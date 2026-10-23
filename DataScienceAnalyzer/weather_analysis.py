
# Task 6: Weather Analysis
city_temperature = {
    "nashik": 23,
    "pune": 30,
    "mumbai": 44,
    "delhi": 50,
    "kolkata": -13,
    "bangluru": 10
}


# Weather analysis function
def analyze_weather():
    print("\n--- Weather Analysis ---")

    for city, temperature in city_temperature.items():
        print(city, ":", temperature, "°C")
