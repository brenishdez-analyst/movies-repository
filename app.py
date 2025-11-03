import pandas as pd
import plotly.express as px
import streamlit as st
     
movie_data = pd.read_csv('movies.csv') # leer los datos
st.header("Popularidad segun genero de peliculas")
# hist_button = st.button('Construir histograma') # crear un botón
build_histogram = st.checkbox('Construir histograma')

     
if build_histogram: # al hacer clic en el botón
     # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos peliculas')
     
     # crear un histograma
     fig = px.histogram(movie_data, x="genres", y="popularity")
     
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

st.header("Ingreso por genero")
disp_button = st.button('Construir grafico de dispersion') # crear un botón

if disp_button: # al hacer clic en el botón
     # escribir un mensaje
     st.write('Creación de un grafico de dispersion para el conjunto de datos peliculas')
     
     # crear un grafico de dispersion
     fig = px.scatter(movie_data, x="genres", y="revenue")
     
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

