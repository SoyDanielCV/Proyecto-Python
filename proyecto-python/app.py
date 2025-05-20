import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore

st.header('Análisis de Anuncios de Coches')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión entre odómetro y precio'):
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)