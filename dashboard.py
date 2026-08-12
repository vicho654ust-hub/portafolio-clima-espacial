import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.title("Clima Espacial: Predicción de Tormentas Geomagnéticas")
st.write("Modelo Random Forest entrenado con una década de datos de viento solar (2015-2024).")

modelo = joblib.load("modelo_prediccion_ap.pkl")

st.header("Prueba el modelo con tus propios valores")
col1, col2, col3 = st.columns(3)
bz = col1.slider("Bz (nT)", -50.0, 20.0, -5.0)
velocidad = col2.slider("Velocidad viento solar (km/s)", 250.0, 900.0, 400.0)
densidad = col3.slider("Densidad (n/cc)", 0.1, 30.0, 5.0)

prediccion = modelo.predict(pd.DataFrame({"Bz_nT":[bz], "sw_speed_km_s":[velocidad], "sw_density_n_cc":[densidad]}))
st.metric("Ap predicho", f"{prediccion[0]:.1f}")

st.header("Datos históricos: Bz vs. Ap (2015-2024)")
dataset_final = pd.read_csv("dataset_diario_2015_2024.csv")

fig, ax = plt.subplots()
ax.scatter(dataset_final["Bz_nT"], dataset_final["Ap"], alpha=0.3, s=10)
ax.axvline(bz, color="red", linestyle="--", label="Tu valor de Bz")
ax.set_xlabel("Bz mínimo diario (nT)")
ax.set_ylabel("Ap")
ax.legend()
st.pyplot(fig)