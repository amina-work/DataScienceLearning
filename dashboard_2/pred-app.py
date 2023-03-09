import streamlit as st
import pandas as pd
import plotly_express as px

from PIL import Image


st.set_page_config(page_title="Survey Results")
st.header("Survey Results 2021")
st.subheader("Was this tutorial helpful?")


### Datafram
excel_file = '/home/amina/Desktop/per/python-programs/dashboard_2/region_traffic_by_road_type.csv'
sheet_name = 'DATA'

df = pd.read_csv(excel_file)

st.dataframe(df)

traffic_per_region = pd.read_csv(excel_file,
                                 usecols=[2,8])
#traffic_per_region.dropna(inplace=True)

pie_chart = px.pie(traffic_per_region,
                   title="Total No. of Vehicules",
                   values='all_motor_vehicles',
                   names='Region_name')
st.plotly_chart(pie_chart)
