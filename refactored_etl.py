import os
import glob
import logging
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "forest fires & Air Quality")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD") # Ensure this is set in .env
DATA_DIR = os.getenv("DATA_DIR", "./data/forest_fires")

def get_db_connection():
    """Establishes connection to PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        logging.info("Database connection successful")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to database: {e}")
        raise

def get_csv_files(data_dir):
    """
    Finds all MODIS CSV files in the directory.
    Expected naming convention: modis_YYYY_Country.csv
    """
    pattern = os.path.join(data_dir, "modis_*.csv")
    files = glob.glob(pattern)
    if not files:
        logging.warning(f"No CSV files found in {data_dir}")
    return files

def load_data_to_db(conn):
    cursor = conn.cursor()
    
    # Columns to load
    columns = [
        'latitude', 'longitude', "brightness", "scan", "track", 
        "acq_date", "acq_time", "satellite", "instrument", "confidence", 
        "version", "bright_t31", "frp", "daynight", "type"
    ]
    
    csv_files = get_csv_files(DATA_DIR)
    
    for file_path in csv_files:
        filename = os.path.basename(file_path).replace(".csv", "")
        table_name = filename.lower()
        
        try:
            # Check if table exists
            cursor.execute(f"SELECT to_regclass('public.{table_name}')")
            if not cursor.fetchone()[0]:
                logging.warning(f"Table {table_name} does not exist. Skipping.")
                continue

            # Check if data already exists (naive check)
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            if count > 0:
                logging.info(f"Table {table_name} already has {count} rows. Skipping to avoid duplicates.")
                continue

            logging.info(f"Loading {filename} into {table_name}...")
            
            # Read CSV
            df = pd.read_csv(file_path, usecols=columns)
            
            # Bulk Insert using executemany
            # Note: For very large files, consider copy_from or copy_expert for better performance
            insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
            cursor.executemany(insert_query, df.values.tolist())
            
            conn.commit()
            logging.info(f"Successfully loaded {len(df)} rows into {table_name}")
            
        except Exception as e:
            conn.rollback()
            logging.error(f"Error processing file {filename}: {e}")

    cursor.close()

def main():
    if not DB_PASS:
        logging.error("DB_PASSWORD environment variable not set.")
        return

    conn = None
    try:
        conn = get_db_connection()
        load_data_to_db(conn)
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
    finally:
        if conn:
            conn.close()
            logging.info("Connection closed")

if __name__ == "__main__":
    main()
