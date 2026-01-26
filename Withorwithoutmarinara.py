#Weather Branch
import random

weather_conditions = [
    ("☀️ Sunny", 25, "Great weather! Perfect day for a smooth drive."),
    ("☁️ Cloudy", 20, "Cloudy skies today. Drive safe and stay alert."),
    ("🌧️ Rain", 20, "It's raining. Turning on traction control. Drive carefully."),
    ("⛈️ Thunderstorm", 10, "Storm detected! Reduce speed and keep headlights on."),
    ("❄️ Snow", 10, "Snow on the road. Switching to winter safety mode."),
    ("💨 Windy", 10, "Strong winds today. Keep both hands on the wheel."),
    ("🌫️ Fog", 5, "Low visibility. Fog lights activated. Drive slowly.")
]

# Roll chance
roll = random.randint(1, 100)

current = 0

print("🚗 Smart Car Assistant")
print("----------------------")

for weather, chance, message in weather_conditions:
    current += chance

    if roll <= current:
        print(f"Weather: {weather}")
        print(f"System Message: {message}")
        print(f"Safety Level: {chance}% probability")
        break
