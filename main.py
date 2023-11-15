import streamlit as st
import plotly.express as px
import pandas as pd


def get_data(days):
    dates = ['2022-25-10', "2022-26-10", '2022-27-10']
    temp = [10, 11, 15]
    temp = [days * i for i in temp]
    return dates, temp


st.set_page_config(layout='wide')

st.title('Weather Forecast for next Days')

place = st.text_input('Place: ')

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help='Select the number of forecasted days')

option = st.selectbox('Data to view', ('Temperature', 'Sky'))

st.subheader(f"Temperature for the next {days} days in {place}")

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temp(C)'})
st.plotly_chart(figure)


