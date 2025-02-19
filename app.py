import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Anuncios de Venta de Coches")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para generar histograma
if st.button("Mostrar Histograma de Kilometraje"):
    st.write("Distribución del kilometraje (odómetro)")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Botón para generar gráfico de dispersión
if st.button("Mostrar Gráfico de Dispersión"):
    st.write("Relación entre precio y kilometraje")
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje")
    st.plotly_chart(fig)