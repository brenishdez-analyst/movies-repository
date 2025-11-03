import pandas as pd
import plotly.express as px
import streamlit as st
     
movie_data = pd.read_csv('movies.csv') # leer los datos
st.header("Proyecto Sprint 7 :)")

st.header("Data Viewer")

data = pd.DataFrame(movie_data, columns=['genres','original_title' ,'popularity', 'revenue'])
st.write(data)

st.header("Popularidad según género de películas:")
# hist_button = st.button('Construir histograma') # crear un botón
build_histogram = st.checkbox('Da click en la casilla para generar el histograma')

     
if build_histogram: # al hacer clic en el botón
     # escribir un mensaje
     st.write('Histograma de popularidad según el género de películas')
     
     # crear un histograma
     fig = px.histogram(movie_data, x="genres", y="popularity")
     
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

st.header("Ganancias por género:")
disp_button = st.button('Da click aquí') # crear un botón

if disp_button: # al hacer clic en el botón
     # escribir un mensaje
     st.write('Gráfico de dispersión para determinar las ganancias obtenidas por género')
     
     # crear un grafico de dispersion
     fig = px.scatter(movie_data, x="genres", y="revenue")
     
     # mostrar un gráfico Plotly interactivo
     st.plotly_chart(fig, use_container_width=True)

