celsius  = input("Input temperature in celsius")
result = None
if float(celsius) < -273.15:
    result = ('Error: Temperature below absolute zero (-273.15°С)')
    print(result)
else:
    c = float(celsius)
    f = (c*(9/5)+32)
    result = f
    print(f"{celsius}°C is equivalent to {result}°F")
