import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="DashCOVID", layout="wide")

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country',
               title = 'Número de casos acumulados')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)
