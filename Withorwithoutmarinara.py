#Weather Branch
import random
import datetime

weather_data = {
    "☀️ Sunny": {
        "chance": 25,
        "messages": [
            "Clear skies. Perfect driving conditions.",
            "Sunny and warm today.",
            "Great weather for travel."
        ],
        "speed": ["55–65 mph", "60–70 mph"],
        "climate": "AC",
        "start": False,
        "alarm_offset": 0
    },

    "☁️ Cloudy": {
        "chance": 20,
        "messages": [
            "Cloudy but stable weather.",
            "Low sunlight detected.",
            "Overcast conditions."
        ],
        "speed": ["50–60 mph", "45–55 mph"],
        "climate": "Off",
        "start": False,
        "alarm_offset": 5
    },

    "🌧️ Rain": {
        "chance": 20,
        "messages": [
            "Rain detected. Roads may be slippery.",
            "Wet surface conditions.",
            "Traction control enabled."
        ],
        "speed": ["40–50 mph", "35–45 mph"],
        "climate": "Defrost + AC",
        "start": True,
        "alarm_offset": 10
    },

    "⛈️ Thunderstorm": {
        "chance": 10,
        "messages": [
            "Severe weather detected.",
            "Heavy rain and lightning.",
            "Storm mode activated."
        ],
        "speed": ["25–35 mph", "20–30 mph"],
        "climate": "Defrost + AC",
        "start": True,
        "alarm_offset": 15
    },

    "❄️ Snow": {
        "chance": 10,
        "messages": [
            "Snow detected. Warming vehicle.",
            "Possible ice on roads.",
            "Winter mode enabled."
        ],
        "speed": ["20–30 mph", "15–25 mph"],
        "climate": "Heat",
        "start": True,
        "alarm_offset": 20
    },

    "💨 Windy": {
        "chance": 10,
        "messages": [
            "Strong winds detected.",
            "Vehicle stability reduced.",
            "Crosswind alerts enabled."
        ],
        "speed": ["45–55 mph", "40–50 mph"],
        "climate": "Off",
        "start": False,
        "alarm_offset": 5
    },

    "🌫️ Fog": {
        "chance": 5,
        "messages": [
            "Fog detected. Visibility reduced.",
            "Low visibility ahead.",
            "Fog lights activated."
        ],
        "speed": ["25–35 mph", "20–30 mph"],
        "climate": "Defrost",
        "start": True,
        "alarm_offset": 10
    }
}


# User normal wake-up time
normal_alarm = datetime.time(7, 0)  # 7:00 AM


# Convert time + minutes
def adjust_time(base_time, minutes):
    base = datetime.datetime.combine(
        datetime.date.today(), base_time
    )
    new_time = base + datetime.timedelta(minutes=minutes)
    return new_time.time()


# Pick weather
roll = random.randint(1, 100)
current = 0

print("🚗 Smart Car AI System")
print("======================")

for weather, data in weather_data.items():
    current += data["chance"]

    if roll <= current:

        message = random.choice(data["messages"])
        speed = random.choice(data["speed"])
        alarm = adjust_time(normal_alarm, data["alarm_offset"])

        print(f"Weather: {weather}")
        print(f"Assistant: {message}")
        print(f"Recommended Speed: {speed}")
        print()

        # Alarm system
        print("⏰ Alarm System")
        print(f"Wake-up time set to: {alarm.strftime('%I:%M %p')}")

        # Auto start
        print("\n🔑 Auto Start System")
        if data["start"]:
            print("Remote engine start: ENABLED")
        else:
            print("Remote engine start: Not needed")

        # Climate control
        print("\n🌡️ Climate Control")
        print(f"System Mode: {data['climate']}")

        # Final message
        print("\n✅ Vehicle Ready for Departure")
        print("Drive safe. Have a great day!")

        break
