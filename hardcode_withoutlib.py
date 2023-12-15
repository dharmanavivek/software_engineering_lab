a = 0.5
b = 2
c = 1
def weather_model(x):
    return a * x**2 + b * x + c

x_value = 3
result = weather_model(x_value)
print(f"The result for x = {x_value} is: {result}")
