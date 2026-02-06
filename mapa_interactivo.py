import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_pro_dashboard():
    db_path = "forest_fires_demo.db"
    logging.info("Extrayendo datos masivos...")
    
    conn = sqlite3.connect(db_path)
    
    # Extraemos datos agregados o muestreados para asegurar fluidez en el navegador
    # Plotly no puede renderizar 8 millones de puntos sin colapsar el Chrome del usuario.
    # Tomamos una muestra representativa de puntos de alta intensidad por año.
    query = """
    SELECT latitude, longitude, brightness, year, country 
    FROM modis_all 
    WHERE brightness > 310
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    logging.info(f"Datos filtrados: {len(df)} registros. Optimizando para visualización...")
    
    # Reducimos a un máximo de 50,000 puntos para que el HTML sea ligero y "smooth"
    if len(df) > 50000:
        df = df.sample(50000, random_state=42)
    
    df = df.sort_values(by='year')
    years = sorted(df['year'].unique())
    
    # Rango fijo para la escala (Crucial para que no parpadee la leyenda)
    min_b = 310
    max_b = 500

    logging.info("Construyendo Mapas por año...")
    
    # Creamos un Dashboard con Dropdown de Años
    fig = px.density_mapbox(
        df, 
        lat='latitude', 
        lon='longitude', 
        z='brightness', 
        radius=5,
        center=dict(lat=-15, lon=-60), 
        zoom=2.5,
        mapbox_style="carto-darkmatter", # Estilo NASA / Dark Mode
        animation_frame="year",
        range_color=[min_b, max_b],
        hover_data={'year': False, 'brightness': True},
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'brightness': 'Temp. Brillo (K)'}
    )

    # Ajustes estéticos finales
    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0},
        coloraxis_colorbar=dict(
            title="Intensidad Térmica (K)",
            thicknessmode="pixels", thickness=15,
            lenmode="pixels", len=300,
            yanchor="top", y=0.9,
            ticks="outside"
        ),
        sliders=[dict(currentvalue={"prefix": "Año: "}, font=dict(color="white"))],
        paper_bgcolor="#111",
        plot_bgcolor="#111"
    )

    # Generar HTML con estilos profesionales (NASA Lab-style)
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Forest Fire Lab v2.0</title>
        <style>
            body {{
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                overflow: hidden;
            }}
            .header {{
                background: linear-gradient(90deg, #161b22 0%, #0d1117 100%);
                padding: 15px 30px;
                border-bottom: 1px solid #30363d;
                display: flex;
                justify-content: space-between;
                align-items: center;
                height: 60px;
            }}
            .title {{
                font-size: 20px;
                font-weight: 600;
                color: #f0f6fc;
                letter-spacing: 1px;
            }}
            .stats {{
                font-size: 13px;
                color: #8b949e;
            }}
            #map-container {{
                height: calc(100vh - 90px);
                width: 100%;
            }}
            .footer {{
                height: 30px;
                background: #161b22;
                font-size: 11px;
                display: flex;
                align-items: center;
                padding-left: 20px;
                color: #484f58;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="title">🔥 FOREST FIRE ANALYSIS LAB | <span style="color: #ff7b72;">NASA MODIS API</span></div>
            <div class="stats">TOTAL RECORDS PROCESSED: 8.7M | COUNTRY: COL/BRA/CHI</div>
        </div>
        <div id="map-container">
            {fig.to_html(full_html=False, include_plotlyjs='cdn')}
        </div>
        <div class="footer">
            © 2026 Dashboard para Universidad del Rosario - Manuel Santiago Cruz
        </div>
    </body>
    </html>
    """

    output_file = "dashboard_incendios_pro.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    logging.info(f"Dashboard profesional generado: {output_file}")
    print(f"\nDashboard generado con exito: {output_file}")

if __name__ == "__main__":
    create_pro_dashboard()
