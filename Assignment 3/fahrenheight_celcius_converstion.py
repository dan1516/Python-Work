
temperature = float(input("Enter temperature you want to convert: "))
temp_type = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit): ")
if temp_type == "C":
    if temperature < -273.15:
        print("Temperature cannot be below absolute zero (-273.15°C).")
    else:
        fahrenheit = (temperature * 9/5) + 32
        print(f"{temperature} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
elif temp_type == "F":
    if temperature < -459.67:
        print("Temperature cannot be below absolute zero (-459.67°F).")
    else:
        celsius = (temperature - 32) * 5/9
        print(f"{temperature} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")