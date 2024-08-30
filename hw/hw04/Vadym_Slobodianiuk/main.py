celsius = float(input("Enter the temp in Celsius °C: "))

if celsius < -273.15:
  print("Sorry! You Die in Cold Univerese")
else:
  fahrenheit = (celsius * 9/5) + 32
  print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")