import streamlit as st
import pandas as pd
import plotly.express as px


#from utils.data_processing import clean_data
from src.utils.visualization import odometer_histogram, odometer_price_scatterplot


# Load data

car_data = pd.read_csv('vehicles_us.csv') # leer los datos


st.header('Sprint 7: Vehicle Analysis Project')


# Charts with buttons
#if st.button("Generar hisotagrama"):
#    st.plotly_chart(odometer_histogram(car_data), use_container_width=True)

#if st.button("Generar grafico de distribución"):
#    st.plotly_chart(odometer_price_scatterplot(car_data), use_container_width=True)




# Charts built with checkboxs
build_histogram = st.checkbox('Generate Histogram')
if build_histogram:
    st.write('Histogram for the Odometer Column')
    st.plotly_chart(odometer_histogram(car_data), use_container_width=True)

build_scatter = st.checkbox('Generate scatterplot')
if build_scatter:
    st.write('Scatter Plot for the Odometer and Price Columns')
    st.plotly_chart(odometer_price_scatterplot(car_data), use_container_width=True)
