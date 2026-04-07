#Task 1: Build Smart Agent

#Extend current agent:

 #Add:

#Weather API tool
#File reader tool

#Input:

#"Check weather in Bangalore"

import requests

# TOOL 1: Weather API (Using Open-Meteo free tier)
def get_weather(city):
    # Get coordinates for the city first
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()
    
    if "results" not in geo_data:
        return f"Sorry, I couldn't find {city}."
    
    lat, lon = geo_data["results"][0]["latitude"], geo_data["results"][0]["longitude"]
    
    # Get actual weather
    w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    w_data = requests.get(w_url).json()
    temp = w_data["current_weather"]["temperature"]
    return f"The current temperature in {city} is {temp}°C."

# TOOL 2: File Reader
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

# THE AGENT LOGIC (Simple Dispatcher)
def smart_agent(user_input):
    user_input = user_input.lower()
    
    if "weather in" in user_input:
        city = user_input.split("in ")[-1].strip()
        return get_weather(city)
    
    elif "read file" in user_input:
        filename = user_input.split("file ")[-1].strip()
        return read_file(filename)
    
    return "I'm not sure how to help with that yet!"

# TEST IT
print(smart_agent("Check weather in Bangalore"))