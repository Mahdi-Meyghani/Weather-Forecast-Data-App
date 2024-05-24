import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter name of the City")
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {place}")


def get_data(day):
    dates = ["2024-24-10", "2024-25-10", "2024-26-10"]
    temperatures = [10, 11, 20]

    temperatures = [i * day for i in temperatures]

    return dates, temperatures


d, t = get_data(days)
