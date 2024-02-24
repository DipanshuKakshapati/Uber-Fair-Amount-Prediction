import streamlit as st
import pandas as pd
import pickle
import time

# Load your trained model
model_data = pickle.load(open('uber_fare_amount_prediction.pkl', 'rb'))
model = model_data['model']
model_accuracy = model_data['accuracy']
# Assuming 'logo.png' is the path to your logo image file
st.sidebar.image('logo.png', use_column_width=True)

# Add formatted text below the logo in the sidebar
st.sidebar.markdown("""
    **About the Company**  
    Ride-sharing services like Uber have revolutionized transportation by providing convenient and affordable rides. As a data scientist, your task is to predict the fare amount of future rides using regression analysis. By accurately estimating the fare amount, ride-sharing companies can optimize pricing strategies, provide transparency to riders, and ensure fair compensation for drivers.

    **Bridging the gap**  
    The fare amount of a ride is influenced by various factors such as distance, duration, traffic conditions, time of day, and demand. Your goal is to develop a regression model that can predict the fare amount based on these factors. You will work with a dataset that includes historical ride data, including the fare amount and relevant features.
""", unsafe_allow_html=True)

st.title('Predict the Fare Amount of Future Rides')

st.image('logo.png')

st.write("""
This is a regression model to predict the fare amount of future rides.
""")
         
# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Pickup longitude
""")
# Replace selectbox with st.radio
pickup_longitude = st.number_input('Pickup longitude')

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Pickup latitude 
""")
# Rest of your st.radio widgets replacing selectbox...
pickup_latitude = st.number_input('Pickup latitude')

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Dropoff longitude
""")
dropoff_longitude = st.number_input('Dropoff longitude')

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Dropoff latitude
""")
dropoff_latitude = st.number_input('Dropoff latitude')

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Passenger count
""")
passenger_count = st.slider('Number of passengers', 1, 8, 1)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Pickup year
""")
pickup_year = st.selectbox('Select your department', ['2009','2010','2011','2012','2013','2014','2015'])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Pickup month 
""")
pickup_month  = st.selectbox('Select your department', ['January','February','March','April','May','June','July', 'August','September','October','November','December'])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Pickup weekday 
""")
pickup_weekday  = st.selectbox('Select your department', ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Pickup hour
0 is 12 AM. 23 is 11 PM
""")
pickup_hour = st.slider('Previous Year Rating', 0, 23, 1)

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

st.write("""
### Distance km 
Distance is in km.
""")
distance_km  = st.number_input('Distance in km')

# Add an empty Markdown to create more space
st.markdown('<br>', unsafe_allow_html=True)

# Processing the prediction when the user changes any input
input_data = {
    'pickup_longitude': [pickup_longitude],
    'pickup_latitude': [pickup_latitude],
    'dropoff_longitude': [dropoff_longitude],
    'dropoff_latitude': [dropoff_latitude],
    'passenger_count': [passenger_count],
    'pickup_year': [pickup_year],
    'pickup_month': [pickup_month],
    'pickup_weekday': [pickup_weekday],
    'pickup_hour': [pickup_hour],
    'distance_km': [distance_km]
}

input_df = pd.DataFrame.from_dict(input_data)

# Display button and make prediction
if st.button('Predict Fare Amount'):
    # Show a loading animation using an animated GIF
    with st.spinner('Predicting...'):
        # Simulate a time-consuming task
        time.sleep(2)
        prediction = model.predict(input_df)
    
    st.markdown(f"Fare Amount: ${prediction[0]:.2f}")
    st.write(f'Model Accuracy: {model_accuracy*100:.2f}%')

    st.balloons()
