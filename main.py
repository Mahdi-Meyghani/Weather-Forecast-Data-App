import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input(label="Place", placeholder="Enter name of the City")
place = place.title()
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

if place:
    st.subheader(f"{option} for the next {days} days in {place}")
    try:
        filtered_content = get_data(place, days)

        dates = [value["dt_txt"] for value in filtered_content]

        if option == "Temperature":

            temperatures = [value["main"]["temp"] / 10 for value in filtered_content]

            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            weathers = [value["weather"][0]["main"] for value in filtered_content]

            images = {"Clear": "images/clear.png", "Rain": "images/rain.png", "Snow": "images/snow.png",
                      "Clouds": "images/cloud.png"}

            images_path = [images[condition] for condition in weathers]

            st.image(images_path, caption=dates, width=170)
    except KeyError:
        st.header("The place doesn't exist")