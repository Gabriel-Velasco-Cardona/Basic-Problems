print("Celsius\tFahrenheit")
print("-" * 21)

for celsius in range(0, 101, 10):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C\t\t{fahrenheit}°F")