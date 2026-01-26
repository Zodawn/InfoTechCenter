#Weather Branch
import random

weather_conditions = [
    ("☀️ Sunny", 25),
    ("☁️ Cloudy", 20),
    ("🌧️ Rain", 20),
    ("⛈️ Thunderstorm", 10),
    ("❄️ Snow", 10),
    ("💨 Windy", 10),
    ("🌫️ Fog", 5)
]

# Pick one weather based on chance
random_number = random.randint(1, 100)

current = 0

for weather, chance in weather_conditions:
    current += chance

    if random_number <= current:
        print("Today's Weather Forecast")
        print("------------------------")
        print(f"Condition: {weather}")
        print(f"Chance Roll: {random_number}%")
        break
