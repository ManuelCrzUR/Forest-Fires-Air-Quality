import psycopg2
import pandas as pd

connection = None  # Inicializa la variable connection fuera del bloque try

try:
    connection = psycopg2.connect(
       host="localhost",
       database="forest fires & Air Quality", #el nombre que se le haya puesto al DB al crearlo en sql
       user="postgres",
       password="123456789" #poner contraseña propia
   )
    print('Conexión exitosa' + "\n")
    
    cursor = connection.cursor()
    
    # Visualicar las tablas de la base de datos
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print(table[0])
        
    print("\n")
        
    # Contar tablas en la base de datos
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public'")
    table_count = cursor.fetchone()[0]
    print(f"Cantidad de tablas en la base de datos: {table_count}" + "\n")
    
    # Cargar datos desde multiples archivos CSV a la base de datos
    
    # ruta CSV
    ruta_csv = "C:/Users/manue/Desktop/work/INS_AQ&FF/data/forest_fires"
    
    # nombres de los archivos CSV
    archivos = ["modis_2010_Brazil", "modis_2011_Brazil", "modis_2012_Brazil", 
                "modis_2013_Brazil", "modis_2014_Brazil", "modis_2015_Brazil",
                "modis_2016_Brazil", "modis_2017_Brazil", "modis_2018_Brazil",
                "modis_2019_Brazil", "modis_2020_Brazil", "modis_2010_Colombia",
                "modis_2011_Colombia", "modis_2012_Colombia", "modis_2013_Colombia",
                "modis_2014_Colombia", "modis_2015_Colombia", "modis_2016_Colombia",
                "modis_2017_Colombia", "modis_2018_Colombia", "modis_2019_Colombia",
                "modis_2020_Colombia", "modis_2010_Chile", "modis_2011_Chile",
                "modis_2012_Chile", "modis_2013_Chile", "modis_2014_Chile",
                "modis_2015_Chile", "modis_2016_Chile", "modis_2017_Chile",
                "modis_2018_Chile", "modis_2019_Chile", "modis_2020_Chile"]
    
    # columnas de las tablas
    columnas = ['latitude', 'longitude', "brightness", "scan", "track", 
    "acq_date", "acq_time", "satellite", "instrument", "confidence", 
    "version", "bright_t31", "frp", "daynight", "type"]
    
    # Consultar el primer dato de la tabla modis_2020_colombia
    print("Verificar que existan datos en DB para no añadirlos de nuevo" + "\n")
    cursor.execute("SELECT * FROM modis_2020_colombia LIMIT 1")
    first_row = cursor.fetchone()  # Obtener la primera fila

    if first_row:
        print("Primer dato de la tabla modis_2020_colombia:", first_row)
    else:
        print("La tabla está vacía")
        c = 0
        for tabla in tables[1:]:
            t = tabla[0].lower()
            a = archivos[c].lower()

            
            if t == a:
                print(f"Cargando datos en la tabla: {t}")

                # Cargar datos desde el archivo CSV
                archivo_csv = f"{ruta_csv}/{archivos[c]}.csv"
                df = pd.read_csv(archivo_csv, usecols=columnas)
                
                # Insertar datos en la tabla
                insert_query = f"INSERT INTO {t} ({', '.join(columnas)}) VALUES ({', '.join(['%s'] * len(columnas))})"
                cursor.executemany(insert_query, df.values.tolist())

                # Confirmar cambios en la base de datos
                connection.commit()
                print(f"Datos insertados en la tabla: {t}")

                c += 1
            else:
                print("diferentes")
                print(f"Error: {a} no coincide con {t}")
                break

except Exception as e:
    print(f"Error: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexión cerrada")
        