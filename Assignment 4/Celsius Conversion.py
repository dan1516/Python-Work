Celsius = int(input("Enter temperature in Celsius: "))
while Celsius < -273.15:
    print("Temperature cannot be below absolute zero (-273.15°C).")
    Celsius = int(input("Enter temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
print('Celsius\t     Fahrenheit')
print('-----------------------------')
for Celsius in range(1, Celsius + 1):
    Fahrenheit = (Celsius * 9/5) + 32
    print(f'{Celsius}\t     {Fahrenheit:.2f}')