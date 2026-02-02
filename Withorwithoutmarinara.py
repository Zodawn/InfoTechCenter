# Gasoline Branch

# =====================================
# SMART CAR GAS & ALARM SYSTEM (PYTHON)
# =====================================

import random
import datetime


# -------------------------------------
# SIMULATED GAS SENSOR
# -------------------------------------
# This creates a fake gas level (0–100%)
# In a real car, this would come from sensors
gas_percent = random.randint(5, 100)


# -------------------------------------
# GAS STATION DATABASE (FAKE DATA)
# -------------------------------------
# Each station has:
# name, price, snacks, drinks

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
# Your regular wake-up time
normal_alarm = datetime.time(7, 0)


# -------------------------------------
# FUNCTION: ADJUST TIME
# -------------------------------------
# Adds or subtracts minutes from a time

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
# Decides how early to wake up

def gas_alarm_adjust(gas):

    if gas <= 15:
        return 30      # Very low gas

    elif gas <= 30:
        return 20      # Low gas

    elif gas <= 50:
        return 10      # Medium gas

    else:
        return 0       # Gas is good


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
# SHOW GAS STATIONS
# -------------------------------------

print("\n🏪 Nearby Gas Stations")
print("----------------------")

for station in gas_stations:

    print(f"\n📍 {station['name']}")
    print(f"💲 Price: ${station['price']} / gallon")

    print("🍿 Snacks:")
    for snack in station["snacks"]:
        print(f"  - {snack}")

    print("🥤 Drinks:")
    for drink in station["drinks"]:
        print(f"  - {drink}")


# -------------------------------------
# FIND CHEAPEST STATION
# -------------------------------------

cheapest = min(gas_stations, key=lambda x: x["price"])


print("\n💰 Cheapest Gas")
print("--------------")
print(f"{cheapest['name']} - ${cheapest['price']} / gallon")


# -------------------------------------
# ADJUST ALARM
# -------------------------------------

offset = gas_alarm_adjust(gas_percent)

# Negative = wake up earlier
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
