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
    print('Conexión exitosa')
    
    cursor = connection.cursor()
    
    # Visualicar las tablas de la base de datos
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()
    print("Tablas en la base de datos:")
    for table in tables:
        print(table[0])
        
    # Contar tablas en la base de datos
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public'")
    table_count = cursor.fetchone()[0]
    print(f"Cantidad de tablas en la base de datos: {table_count}")
    
except:
    print('Error de conexión')