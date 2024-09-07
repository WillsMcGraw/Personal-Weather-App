import requests
import json

api_key = "3903213a8131c3c0656d68c55112b07b"

city = "Blacksburg"
state_code = "VA"
country_code = "US"

city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_code},{country_code}&appid={api_key}"
coordinates = requests.get(city_url).json()[0]
longitude = coordinates["lon"]
latitude = coordinates["lat"]
print(longitude)
print(latitude)


# url = ""
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     data = json.dumps(data)
#     print(data)
# else:
#     print("Error in fetching data")