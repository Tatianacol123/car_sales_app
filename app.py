
import pandas as pd
import plotly.express as px
import streamlit as st

# Creación de Título para la App
st.title("Car Sales App - Sprint 7")

st.write("Con esta aplicación podrás visualizar datos de vehículos y crear gráficos.")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
st.divider()

# Botón para histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True, key="hist_btn")

# Checkbox para histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig_2 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_2, use_container_width=True, key="hist_chk")

st.divider()

# **Sección de gráfico de dispersión**
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write("Gráfico de dispersión: precio vs. odómetro")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)