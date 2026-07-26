# Real-Time Weather & Currency Data Fetcher
# ------------------------------------------
# A command-line tool that fetches live weather data (wttr.in) and
# currency exchange rates (open.er-api.com), and can save/view the
# most recently fetched result in a local JSON file.
# """
 
import json
import os
from datetime import datetime
 
import requests

 
# -----------------------------------------------------
# 1. Current Weather
# -----------------------------------------------------
def weather():
   
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.\n")
        return None
 
    url = f"https://wttr.in/{city}?format=j1"
 
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()          # raises an error for 4xx/5xx responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch weather data: {e}\n")
        return None
    except ValueError:
        print("Server did not return valid JSON.\n")
        return None
 
    try:
        current = data["current_condition"][0]
        temperature = int(current["temp_C"])
        humidity = int(current["humidity"])
        wind_speed = int(current["windspeedKmph"])
        condition = current["weatherDesc"][0]["value"]
    except (KeyError, IndexError):
        print("Unexpected response format from weather API.\n")
        return None
 
    now = datetime.now()
    display_time = now.strftime("%d-%m-%Y %I:%M %p")
    storage_time = now.strftime("%Y-%m-%d %H:%M:%S")
 
    print("\n------ Weather Report ------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"Condition: {condition}")
    print(f"Fetched At: {display_time}")
    print("----------------------------\n")
 
    return {
        "type": "weather",
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "condition": condition,
        "time": storage_time,
    }
 
 
# -----------------------------------------------------
# 2. Currency Exchange Rate
# -----------------------------------------------------
def currency():
    
    base = input("Base Currency: ").strip().upper()
    target = input("Target Currency: ").strip().upper()
 
    if not base or not target:
        print("Both currency codes are required.\n")
        return None
 
    url = f"https://open.er-api.com/v6/latest/{base}"
 
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch exchange rate: {e}\n")
        return None
    except ValueError:
        print("Server did not return valid JSON.\n")
        return None
 
    if data.get("result") != "success":
        print("API could not process that base currency.\n")
        return None
 
    rates = data.get("rates", {})
    if target not in rates:
        print(f"Target currency '{target}' not found.\n")
        return None
 
    rate = rates[target]
    now = datetime.now()
    display_time = now.strftime("%d-%m-%Y %I:%M %p")
    storage_time = now.strftime("%Y-%m-%d %H:%M:%S")
 
    print(f"\n1 {base} = {rate:.2f} {target}")
    print(f"Fetched At: {display_time}\n")
 
    return {
        "type": "currency",
        "base": base,
        "target": target,
        "rate": round(rate, 2),
        "time": storage_time
    }
 
 
# -----------------------------------------------------
# 3. Save Result to data.json
# -----------------------------------------------------
def save_json(latest_result):
 
    if latest_result is None:
        print("Nothing to save yet — fetch weather or currency data first.\n")
        return
 
    try:
        with open("data.json", "w") as f:
            json.dump(latest_result, f, indent=4)
        print("Data saved to data.json\n")
    except IOError as e:
        print(f"Error saving data: {e}\n")
 
 
# -----------------------------------------------------
# 4. View Previously Saved Data
# -----------------------------------------------------
def view_json():
 
    if not os.path.exists("data.json"):
        print("No saved data found yet. Use option 3 to save some first.\n")
        return
 
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading saved data: {e}\n")
        return
 
    print("\n------ Last Saved Data ------")
    if data.get("type") == "weather":
        print("Type: Weather")
        print(f"City: {data.get('city')}")
        print(f"Temperature: {data.get('temperature')}°C")
        print(f"Humidity: {data.get('humidity')}%")
        print(f"Wind Speed: {data.get('wind_speed')} km/h")
        print(f"Condition: {data.get('condition')}")
    elif data.get("type") == "currency":
        print("Type: Currency")
        print(f"1 {data.get('base')} = {data.get('rate')} {data.get('target')}")
    else:
        print("Unknown data type in file.")
    print(f"Saved Time: {data.get('time')}")
    print("------------------------------\n")
 
 
# -----------------------------------------------------
# 5. Main Menu
# -----------------------------------------------------
def main_menu():
 
    latest_result = None
 
    while True:
        print("========== Data Fetcher ==========")
        print("1. Current Weather")
        print("2. Currency Exchange Rate")
        print("3. Save Result to JSON File")
        print("4. View Previous Saved Data")
        print("5. Exit")
        print("==================================")
 
        choice = input("Enter your choice (1-5): ").strip()
 
        if choice == "1":
            result = weather()
            if result is not None:
                latest_result = result
        elif choice == "2":
            result = currency()
            if result is not None:
                latest_result = result
        elif choice == "3":
            save_json(latest_result)
        elif choice == "4":
            view_json()
        elif choice == "5":
            print("\nThank You")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
 
 
# -----------------------------------------------------
# Program Starts Here
# -----------------------------------------------------
if __name__ == "__main__":
    main_menu()
 
