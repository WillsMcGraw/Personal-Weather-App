import requests
import json

# Creates an empty dictionary for config variables to be stored in
env_config = {}

# Opens the JSON files holding the config information and stores them
# in the env_config dictionary
with open('config.json', 'r') as config_json:
    config = json.load(config_json)
    env_config['key'] = config['key']
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
weather_data = requests.get(weather_url).json()
print(weather_data)