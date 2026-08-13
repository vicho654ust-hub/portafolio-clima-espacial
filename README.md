# Clima Espacial y Precisión GNSS/GPS

Proyecto de investigación aplicada: análisis del impacto del clima espacial (viento solar, tormentas geomagnéticas, anomalías ionosféricas) sobre fenómenos que afectan la precisión de señales GPS/GNSS. Desarrollado como proyecto de portafolio en Data Science / Machine Learning, con datos reales de la NASA, GFZ Potsdam y NOAA.

## Objetivo

Analizar, con datos reales y un enfoque riguroso, cómo la actividad del viento solar se relaciona con las tormentas geomagnéticas y las anomalías en la ionosfera — evaluando además si existe relación con anomalías gravitacionales terrestres — y construir un modelo capaz de predecir la intensidad de una tormenta geomagnética a partir de variables del viento solar.

Este proyecto no busca un descubrimiento científico nuevo: su valor está en el manejo riguroso de datos reales, la interpretación honesta de los resultados (incluyendo un hallazgo negativo) y la construcción de una herramienta predictiva funcional, de principio a fin.

## Resultados principales

| Análisis | Resultado |
|---|---|
| Correlación Bz (viento solar) vs. índice Ap | **-0.81** (fuerte, inversa) |
| Correlación velocidad del viento solar vs. Ap | 0.05 (prácticamente nula) |
| Anomalía de TEC ionosférico, tormenta vs. día tranquilo | Anomalía real confirmada (10 mayo 2024) |
| Correlación espacial: gravedad (EGM2008) vs. anomalía de TEC | **-0.05** (hallazgo negativo: no hay evidencia de relación) |
| Modelo Random Forest (Bz, velocidad, densidad → Ap) | R² = 0.656, error absoluto promedio = 2.96 |
| Modelo de regresión lineal (mismas variables) | R² = 0.601, error absoluto promedio = 3.45 |

Variable más importante para el modelo: **Bz** (orientación del campo magnético interplanetario), muy por sobre velocidad y densidad del viento solar.

## Estructura del proyecto

```
├── notebooks/              # Análisis exploratorio y entrenamiento del modelo
├── dashboard.py             # Dashboard interactivo (Streamlit)
├── modelo_prediccion_ap.pkl # Modelo Random Forest entrenado, listo para usar
├── dataset_diario_2015_2024.csv  # Dataset diario procesado (2015-2024)
└── README.md
```

## Fuentes de datos

- **Índice geomagnético Kp/Ap** — [GFZ Potsdam](https://www-app3.gfz-potsdam.de/kp_index/)
- **Viento solar** (Bz, velocidad, densidad) — [NASA OMNIWeb](https://omniweb.gsfc.nasa.gov/)
- **TEC ionosférico (IONEX)** — [NASA CDDIS](https://cddis.nasa.gov/)
- **Anomalía gravitacional (EGM2008)** — [ICGEM, GFZ Potsdam](http://icgem.gfz-potsdam.de/)

## Metodología (resumen)

1. **Análisis de causa-efecto**: viento solar (Bz, velocidad) vs. índice Ap, usando el mínimo/máximo diario en vez de promedios, para no diluir los picos de tormenta.
2. **Anomalías ionosféricas**: comparación de mapas globales de TEC entre un día de tormenta y un día tranquilo de referencia.
3. **Prueba de hipótesis espacial**: correlación entre anomalías de TEC y anomalías gravitacionales terrestres, en miles de puntos del planeta.
4. **Modelado predictivo**: Random Forest y regresión lineal, entrenados con una década de datos horarios (2015-2024), evaluados con train/test split.
5. **Dashboard interactivo**: interfaz en Streamlit para explorar el modelo con valores personalizados, con contexto histórico visual.

## Cómo ejecutar el dashboard localmente

```bash
conda create -n climaespacial python=3.11 pandas matplotlib jupyter scikit-learn streamlit
conda activate climaespacial
streamlit run dashboard.py
```

## Stack técnico

Python · pandas · scikit-learn · matplotlib · Streamlit · Git/GitHub

## Estado del proyecto

Análisis técnico y dashboard completos. Documento de investigación (LaTeX) en desarrollo.

## Autor

Proyecto desarrollado por [tu nombre] como parte de un portafolio profesional en Data Science / Machine Learning.
