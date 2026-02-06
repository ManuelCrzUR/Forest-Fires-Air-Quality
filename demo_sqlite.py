import sqlite3
import pandas as pd
import os
import glob
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ruta de los datos (verificada en pasos anteriores)
DATA_DIR = r"C:\Users\manue\Desktop\work\INS_AQ&FF\data\forest_fires"
DB_FILE = "forest_fires_demo.db"

def run_demo():
    # 1. Conexión a SQLite (crea el archivo si no existe)
    logging.info(f"Conectando a la base de datos local: {DB_FILE}")
    conn = sqlite3.connect(DB_FILE)
    
    # 2. Definición de columnas
    columns = [
        'latitude', 'longitude', "brightness", "scan", "track", 
        "acq_date", "acq_time", "satellite", "instrument", "confidence", 
        "version", "bright_t31", "frp", "daynight", "type"
    ]
    
    # 3. Buscar archivos CSV
    csv_files = glob.glob(os.path.join(DATA_DIR, "modis_*.csv"))
    if not csv_files:
        logging.error("No se encontraron archivos CSV en la ruta especificada.")
        return

    logging.info(f"Se encontraron {len(csv_files)} archivos para procesar.")

    # 4. Procesamiento y Carga (Subset para velocidad)
    for file_path in csv_files:
        filename = os.path.basename(file_path).replace(".csv", "")
        logging.info(f"Procesando {filename}...")
        
        try:
            # Quitamos el límite de 1000 filas para cargar TODOS los datos
            df = pd.read_csv(file_path, usecols=columns)
            
            # Agregar columna de país e información de año extraída del nombre
            parts = filename.split('_')
            df['year'] = parts[1]
            df['country'] = parts[2]
            
            # Cargar a SQLite
            df.to_sql("modis_all", conn, if_exists='append', index=False)
        except Exception as e:
            logging.error(f"Error cargando {filename}: {e}")

    logging.info("¡Carga completada con éxito!")

    # 5. Análisis rápido de los datos cargados
    logging.info("--- Resumen de Datos Cargados ---")
    query = """
    SELECT country, year, COUNT(*) as registros, AVG(frp) as avg_frp
    FROM modis_all
    GROUP BY country, year
    LIMIT 10;
    """
    resumen = pd.read_sql_query(query, conn)
    print("\n")
    print(resumen.to_string(index=False))
    print("\n")

    conn.close()

if __name__ == "__main__":
    run_demo()
