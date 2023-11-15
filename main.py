import streamlit as st
import plotly.express as px
import pandas as pd
import backend

st.title('Weather Forecast for next Days')

place = st.text_input('Place: ')

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help='Select the number of forecasted days')

option = st.selectbox('Data to view', ('Temperature', 'Sky'))



if place:
    filtered_data = backend.get_data(place=place, forecast_days=days)
    if option == 'Temperature':
        st.subheader(f"Temperature for the next {days} days in {place}")
        temperatures = [dict['main']['temp']/10 for dict in filtered_data]
        days = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=days, y=temperatures, labels={'x': 'Date', 'y': 'Temp(C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        sky = [dict['weather'][0]['main'] for dict in filtered_data]
        images = {'Clear': 'images/clear.png',
                  'Clouds': 'images/cloud.png',
                  'Rain': 'images/rain.png',
                  'Snow': 'images/snow.png'}
        image = [images[condition] for condition in sky]
        st.subheader(f"Sky condition in next {days} days")
        st.image(image, width=150)



