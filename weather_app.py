from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

print("Welcome to Tommy's Weather App")
print("Enter city name")

user_input = input()
user_input = user_input.lower()
formatted_input = f'{user_input}'

location = weather.lookup_by_location(formatted_input)

forcasts = location.forecast
for forecast in forcasts:
    w_date = forecast.date
    w_text = forecast.text
    w_high = forecast.high
    w_low = forecast.low

# (°C × 9/5) + 32 = °F
w_high = int((int(w_high) * (9/5)) + 32)
w_low = int((int(w_low) * (9/5)) + 32)

w_high = str(w_high)
w_low = str(w_low)


print("Todays weather in " + user_input.capitalize() + ":")
print(w_text)
print("High of " + w_high + " with a low of " + w_low)

