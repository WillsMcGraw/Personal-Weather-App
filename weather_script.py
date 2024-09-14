import requests
import json
import datetime

def main():
    # Creates an empty dictionary for config variables to be stored in
    env_config = {}

    # Opens the JSON files holding the config information and stores them
    # in the env_config dictionary
    with open('config.json', 'r') as config_json:
        config = json.load(config_json)
        env_config['key'] = config['weather_key']
        env_config['city'] = config['city']
        env_config['state_code'] = config['state_code']
        env_config['country_code'] = config['country_code']

    # Renames the env_config variables into global variables for ease of use
    KEY = env_config['key']
    CITY = env_config['city']
    STATE = env_config['state_code']
    COUNTRY = env_config['country_code']

    # Pulls weather data using config variables
    weather_url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY},{STATE},{COUNTRY}&appid={KEY}"
    weather_data_full = requests.get(weather_url).json()

    # Slices weather data to only the first 5 entries needed
    weather_data_full = weather_data_full["list"][:5]

    # Creates a dictionary to hold temperature and time data
    weather_data = {'act_temp' : [], 'feel_temp' : [], 'time' : []}

    # Checks through the saved weather data to pull temperature data
    # Temperature data is converted from Kelvin to Fahrenheit and then
    # entered into the previously made dictionary for temperature data
    # It also pulls time data and stores it in the dictionary
    for i in range(len(weather_data_full)):
        a_temp = round(convert_K_to_F(weather_data_full[i]['main']['temp']), 1)
        f_temp = round(convert_K_to_F(weather_data_full[i]['main']['feels_like']), 1)
        time = convert_time(weather_data_full[i]['dt'])
        weather_data['act_temp'].append(a_temp)
        weather_data['feel_temp'].append(f_temp)
        weather_data['time'].append(time)

    return weather_data

# A simple function to convert Kelvin temperatures to
# fahrenheit temperatures
# It returns an integer that represents the temperature in Fahrenheit
def convert_K_to_F(K_temp):
    C_temp = K_temp - 273.15
    F_temp = C_temp * 1.8 + 32
    return F_temp

# A function to take a time in UNIX and convert it to a datetime type.
def convert_time(unix_time):
    converted_time = datetime.datetime.fromtimestamp(unix_time)
    return converted_time

# Runs the main function
if __name__ == "__main__":
    main()