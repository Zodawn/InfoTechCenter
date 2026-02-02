#BeatatestDev

# Welcome Branch
# This program simulates a simple boot-up animation
# using dots that appear and disappear.

# Libraries Imported Here
import sys      # Used to write output on the same line in the terminal
import time     # Used to add delays for animation timing

# ANSI color codes (used to color text in the terminal)
RESET = "\033[0m"    # Resets text color to default
GREEN = "\033[32m"   # Green text
CYAN = "\033[36m"    # Cyan text
YELLOW = "\033[33m"  # Yellow text

# Display startup messages
print(CYAN + "Welcome Branch - Developer: CorDae Clark" + RESET)
print("\n" + GREEN + "Welcome to InfoTechCenter V.1.0" + RESET)

# Counter to control how long the boot animation runs
x = 0

# Controls how many dots appear in the animation
ellipsis = 0

# Loop runs until x reaches 20
while x != 20:
    x += 1  # Increase loop counter

    # Create the boot message with animated dots
    ellipsisMessage = (
        GREEN + "InfoTechCenter OS Booting " +
        YELLOW + "." * ellipsis +
        RESET
    )

    ellipsis += 1  # Add another dot each loop

    # Overwrite the current terminal line with the new message
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Force the update to appear immediately

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dots after reaching 3
    if ellipsis == 4:
        ellipsis = 0

    # When the loop finishes, print the success message
    if x == 20:
        print(
            "\n" + GREEN +
            "Operating System Booted - Retina Scanned - Access Granted" +
            RESET
        )


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

# SMART CAR GAS & ALARM SYSTEM (PYTHON)
# =====================================

import random
import datetime


# -------------------------------------
# SIMULATED GAS SENSOR
# -------------------------------------
# Generate fake gas level (5%–100%)
gas_percent = random.randint(5, 100)


# -------------------------------------
# GAS STATION DATABASE
# -------------------------------------

gas_stations = [

    {
        "name": "Shell",
        "price": 3.45,
        "snacks": ["Chips", "Candy", "Hot Dogs"],
        "drinks": ["Soda", "Energy Drink", "Water"]
    },

    {
        "name": "Exxon",
        "price": 3.39,
        "snacks": ["Nachos", "Cookies", "Jerky"],
        "drinks": ["Tea", "Coffee", "Juice"]
    },

    {
        "name": "BP",
        "price": 3.29,
        "snacks": ["Pretzels", "Donuts", "Sandwiches"],
        "drinks": ["Milk", "Smoothies", "Soda"]
    },

    {
        "name": "7-Eleven",
        "price": 3.55,
        "snacks": ["Slurpee", "Pizza", "Brownies"],
        "drinks": ["Slurpee", "Iced Coffee", "Water"]
    }
]


# -------------------------------------
# NORMAL ALARM TIME
# -------------------------------------

normal_alarm = datetime.time(7, 0)


# -------------------------------------
# FUNCTION: ADJUST TIME
# -------------------------------------

def adjust_time(base_time, minutes):

    base = datetime.datetime.combine(
        datetime.date.today(),
        base_time
    )

    new_time = base + datetime.timedelta(minutes=minutes)

    return new_time.time()


# -------------------------------------
# FUNCTION: GAS → ALARM
# -------------------------------------

def gas_alarm_adjust(gas):

    if gas <= 15:
        return 30

    elif gas <= 30:
        return 20

    elif gas <= 50:
        return 10

    else:
        return 0


# -------------------------------------
# START SYSTEM
# -------------------------------------

print("🚗 Smart Fuel System")
print("===================")


# -------------------------------------
# SHOW GAS LEVEL
# -------------------------------------

print(f"\n⛽ Gas Level: {gas_percent}%")


# -------------------------------------
# GAS WARNING
# -------------------------------------

if gas_percent <= 15:
    print("⚠️ WARNING: Very Low Gas!")

elif gas_percent <= 30:
    print("⚠️ Low Gas - Please Refuel Soon")

else:
    print("✅ Gas Level is Good")


# -------------------------------------
# PICK 2 RANDOM GAS STATIONS
# -------------------------------------

# Select only 2 stations (no repeats)
selected_stations = random.sample(gas_stations, 2)


# -------------------------------------
# SHOW GAS STATIONS
# -------------------------------------

print("\n🏪 Nearby Gas Stations (2 Shown)")
print("-------------------------------")

for station in selected_stations:

    print(f"\n📍 {station['name']}")
    print(f"💲 Price: ${station['price']} / gallon")

    print("🍿 Snacks:")
    for snack in station["snacks"]:
        print(f"  - {snack}")

    print("🥤 Drinks:")
    for drink in station["drinks"]:
        print(f"  - {drink}")


# -------------------------------------
# FIND CHEAPEST OF THE 2
# -------------------------------------

cheapest = min(selected_stations, key=lambda x: x["price"])


print("\n💰 Cheapest Nearby Gas")
print("---------------------")
print(f"{cheapest['name']} - ${cheapest['price']} / gallon")


# -------------------------------------
# ADJUST ALARM
# -------------------------------------

offset = gas_alarm_adjust(gas_percent)

# Wake up earlier if needed
new_alarm = adjust_time(normal_alarm, -offset)


# -------------------------------------
# SHOW ALARM
# -------------------------------------

print("\n⏰ Alarm System")
print("--------------")

if offset > 0:
    print(f"Waking you up {offset} minutes early (Low Gas).")

else:
    print("Normal Wake-Up Time.")

print(f"Wake-Up Time: {new_alarm.strftime('%I:%M %p')}")


# -------------------------------------
# FINAL MESSAGE
# -------------------------------------

print("\n✅ System Ready")
print("Drive Safe 🚙💨")

