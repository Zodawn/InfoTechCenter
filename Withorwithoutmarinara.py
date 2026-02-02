# ==============================
# Weather Branch - Smart Car AI
# ==============================

# Import random module (used to generate random numbers and choices)
import random

# Import datetime module (used to work with time and dates)
import datetime


# --------------------------------
# Weather Database (Main System)
# --------------------------------
# This dictionary stores all possible weather types.
# Each weather type contains:
# - chance: probability of happening (out of 100)
# - messages: things the assistant can say
# - speed: recommended driving speeds
# - climate: car climate mode
# - start: whether auto-start is needed
# - alarm_offset: how many minutes earlier to wake up

weather_data = {

    # Sunny weather settings
    "☀️ Sunny": {
        "chance": 25,  # 25% chance
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

    # Cloudy weather settings
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

    # Rain weather settings
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

    # Thunderstorm weather settings
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

    # Snow weather settings
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

    # Windy weather settings
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

    # Fog weather settings
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


# --------------------------------
# Default Alarm Time
# --------------------------------
# This is the user's normal wake-up time (7:00 AM)

normal_alarm = datetime.time(7, 0)


# --------------------------------
# Function: Adjust Time
# --------------------------------
# This function adds minutes to a time.
# Example: 7:00 AM + 10 minutes = 7:10 AM

def adjust_time(base_time, minutes):

    # Combine today's date with the base time
    base = datetime.datetime.combine(
        datetime.date.today(),
        base_time
    )

    # Add minutes using timedelta
    new_time = base + datetime.timedelta(minutes=minutes)

    # Return only the time part
    return new_time.time()


# --------------------------------
# Random Weather Selection
# --------------------------------

# Generate a random number from 1 to 100
roll = random.randint(1, 100)

# This keeps track of probability ranges
current = 0


# --------------------------------
# System Startup Display
# --------------------------------

print("🚗 Smart Car AI System")
print("======================")


# --------------------------------
# Main Weather Loop
# --------------------------------
# This loop goes through each weather type
# and checks if the random number fits its chance.

for weather, data in weather_data.items():

    # Add this weather's chance to total
    current += data["chance"]

    # Check if roll is inside this weather range
    if roll <= current:

        # Pick a random message
        message = random.choice(data["messages"])

        # Pick a random speed range
        speed = random.choice(data["speed"])

        # Calculate new alarm time
        alarm = adjust_time(
            normal_alarm,
            data["alarm_offset"]
        )

        # --------------------------------
        # Display Weather Info
        # --------------------------------

        print(f"Weather: {weather}")
        print(f"Assistant: {message}")
        print(f"Recommended Speed: {speed}")
        print()

        # --------------------------------
        # Alarm System
        # --------------------------------

        print("⏰ Alarm System")
        print(f"Wake-up time set to: {alarm.strftime('%I:%M %p')}")

        # --------------------------------
        # Auto Start System
        # --------------------------------

        print("\n🔑 Auto Start System")

        # Check if auto start is needed
        if data["start"]:
            print("Remote engine start: ENABLED")
        else:
            print("Remote engine start: Not needed")

        # --------------------------------
        # Climate Control System
        # --------------------------------

        print("\n🌡️ Climate Control")
        print(f"System Mode: {data['climate']}")

        # --------------------------------
        # Final Status
        # --------------------------------

        print("\n✅ Vehicle Ready for Departure")
        print("Drive safe. Have a great day!")

        # Stop the loop after finding one weather
        break
