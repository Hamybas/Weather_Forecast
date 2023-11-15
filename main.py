import streamlit as st

st.set_page_config(layout='wide')

st.title('Weather Forecast for next Days')

place = st.text_input('Place: ')

days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help='Select the number of forecasted days')

option = st.selectbox('Data to view', ('Temperature', 'Sky'))

st.subheader(f"Temperature for the next {days} days in {place}")

#1st.plotly_chart()


