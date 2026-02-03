#Gasoline Branch
# =====================================
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
