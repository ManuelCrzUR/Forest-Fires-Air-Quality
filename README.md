# 🔥 Forest Fire & Air Quality Analysis Lab

![Python](https://img.shields.io/badge/python-3.8+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

> 🚀 **Plataforma de análisis geoespacial y pipeline ETL** para el monitoreo masivo de incendios forestales en Sudamérica (Colombia, Brasil, Chile) utilizando datos satelitales **NASA MODIS** (2010-2020).

## 📊 Vista General
Este proyecto resuelve el desafío de procesar y visualizar grandes volúmenes de datos ambientales (>8.7 millones de registros). Proporciona herramientas para la ingesta de datos, análisis estadístico y una visualización interactiva de nivel profesional.

## ✨ Características Principales
*   **Pipeline ETL Masivo:** Ingesta automatizada de archivos CSV históricos hacia bases de datos estructuradas (PostgreSQL/SQLite).
*   **Dashboard Interactivo (v2.0):** Visualización tipo laboratorio con mapas de calor (Heatmaps) espaciales y selector temporal por año.
*   **Análisis Científico:** Extracción de métricas de intensidad (FRP) y temperatura de brillo (Brightness) por país y año.
*   **Arquitectura Dual:** Compatible con PostgreSQL para entornos de producción y SQLite para portabilidad/demos rápidas.

## 🛠️ Estructura del Proyecto
```text
├── data/                       # Datasets crudos (Ignorado en Git)
├── Tables_setup.sql            # Esquema SQL para PostgreSQL
├── conexion_carga.py           # Script ETL original (PostgreSQL)
├── demo_sqlite.py              # Pipeline portátil (SQLite)
├── visualizar_datos.py         # Script de análisis estadístico y gráficos
├── mapa_interactivo.py         # Generador del Dashboard interactivo
├── dashboard_incendios_pro.html # Visualización final (NASA-Style)
└── README.md
```

## 🚀 Cómo Empezar

### 1. Clonar y Preparar
```bash
git clone https://github.com/ManuelCrzUR/Forest-Fires-Air-Quality.git
cd Forest-Fires-Air-Quality
pip install pandas plotly matplotlib seaborn
```

### 2. Ejecutar el Pipeline (Portátil)
Si quieres probar el sistema de inmediato con los datos locales:
```bash
python demo_sqlite.py
```

### 3. Generar el Análisis Visual
```bash
python visualizar_datos.py
python mapa_interactivo.py
```

## 📈 Visualizaciones
El proyecto genera un Dashboard interactivo (`dashboard_incendios_pro.html`) que permite:
*   Seleccionar años específicos para ver la distribución de focos de calor.
*   Visualizar la intensidad térmica con una escala de colores normalizada.
*   Analizar estadísticas agregadas de más de 10 años de historia ambiental.

---
**Manuel Santiago Cruz Garrote**  
*Estudiante de Matemáticas Aplicadas y Ciencias de la Computación - Universidad del Rosario*
