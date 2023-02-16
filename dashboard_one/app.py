import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Covid-19 Cases in Prison Facilities Dashboard",
    page_icon=":mask:",
    layout='wide'
)

#copy entire path otherwise streamlit localhost would not read it
df = pd.read_csv('/home/amina/Desktop/per/python-programs/dashboard_one/facilities.csv')

#cases_in_alabama = df[(df['facility_state'] == 'Alabama')]

st.dataframe(df)

#print(len(df))

#FOR VISUALAZATION: pip install plotly-express

#print(df.head())