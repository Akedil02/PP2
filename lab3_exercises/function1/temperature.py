
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_input = float(input("Enter Fahrenheit temperature: "))
celsius_output = fahrenheit_to_celsius(fahrenheit_input)

print(f"{fahrenheit_input} Fahrenheit is equal to {celsius_output:.2f} Celsius.")
