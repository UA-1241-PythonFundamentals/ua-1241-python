Temperature = float(input("Enter the temperature in Celsius: "))
if Temperature > -273.15:
    print (f"{Temperature}°C is equivalent to {Temperature * 9/5 + 32}°F")
else:
    print('Error: Temperature below absolute zero (-273.15°C)')