import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_insights():
    conn = sqlite3.connect("forest_fires_demo.db")
    
    # 1. Cargar datos para análisis
    query = "SELECT year, country, frp, brightness FROM modis_all"
    df = pd.read_sql_query(query, conn)
    df['year'] = df['year'].astype(int)
    
    # Configurar estilo
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 6))
    
    # 2. Gráfico: Evolución de la Potencia de Fuego (FRP) por año y país
    sns.lineplot(data=df, x='year', y='frp', hue='country', marker='o', linewidth=2.5)
    
    plt.title('Evolución de la Intensidad de Incendios (FRP) 2010-2020', fontsize=16, fontweight='bold')
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('Promedio Fire Radiative Power (MW)', fontsize=12)
    plt.legend(title='País')
    
    # Guardar el gráfico
    output_path = "tendencia_incendios.png"
    plt.savefig(output_path)
    print(f"\nGrafo generado con exito: {output_path}")
    
    # 3. Mostrar estadísticas clave en consola
    print("\n--- Insights Científicos ---")
    top_incendios = df.groupby(['country', 'year'])['brightness'].mean().sort_values(ascending=False).head(5)
    print("\nTop 5 años/países con mayor temperatura de brillo promedio:")
    print(top_incendios)

    conn.close()

if __name__ == "__main__":
    generate_insights()
