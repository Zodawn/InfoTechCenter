#Weather Branch
import random

weather_data = {
    "☀️ Sunny": {
        "chance": 25,
        "messages": [
            "Roads are clear. Enjoy your drive!",
            "Perfect driving conditions today.",
            "Visibility is excellent."
        ],
        "speed": ["55–65 mph", "60–70 mph", "50–60 mph"]
    },

    "☁️ Cloudy": {
        "chance": 20,
        "messages": [
            "Cloudy skies. Stay focused.",
            "Low sunlight detected.",
            "Mild conditions ahead."
        ],
        "speed": ["50–60 mph", "45–55 mph", "55–60 mph"]
    },

    "🌧️ Rain": {
        "chance": 20,
        "messages": [
            "Wet roads detected.",
            "Reduced tire traction.",
            "Rainfall increasing."
        ],
        "speed": ["40–50 mph", "35–45 mph", "45–50 mph"]
    },

    "⛈️ Thunderstorm": {
        "chance": 10,
        "messages": [
            "Severe storm warning.",
            "Heavy rain and lightning.",
            "Road visibility is low."
        ],
        "speed": ["25–35 mph", "30–40 mph", "20–30 mph"]
    },

    "❄️ Snow": {
        "chance": 10,
        "messages": [
            "Snow buildup detected.",
            "Icy conditions possible.",
            "Slippery roads ahead."
        ],
        "speed": ["20–30 mph", "15–25 mph", "25–35 mph"]
    },

    "💨 Windy": {
        "chance": 10,
        "messages": [
            "Strong crosswinds detected.",
            "Vehicle stability reduced.",
            "Wind gusts incoming."
        ],
        "speed": ["45–55 mph", "40–50 mph", "50–55 mph"]
    },

    "🌫️ Fog": {
        "chance": 5,
        "messages": [
            "Low visibility ahead.",
            "Fog density increasing.",
            "Use fog lights."
        ],
        "speed": ["25–35 mph", "30–40 mph", "20–30 mph"]
    }
}


# Pick weather
roll = random.randint(1, 100)
current = 0

print("🚗 Smart Car Assistant")
print("----------------------")

for weather, data in weather_data.items():
    current += data["chance"]

    if roll <= current:

        message = random.choice(data["messages"])
        speed = random.choice(data["speed"])

        print(f"Weather: {weather}")
        print(f"Assistant: {message}")
        print(f"Recommended Speed: {speed}")
        print(f"System Roll: {roll}%")

        break
