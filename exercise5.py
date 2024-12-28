unit = input("Is this temperature in celsius or fahernheit (C/F):")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in fahernheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurment ")