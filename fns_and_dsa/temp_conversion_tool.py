FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    converted = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted

def convert_to_fahrenheit(celsius):
    converted = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return converted

if __name__ == "__main__":
    Temp_convert = int(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        temperature = convert_to_fahrenheit(Temp_convert)
        print(f"{Temp_convert}°C is {temperature:.2f}°F")
    elif unit == 'F':
        temperature = convert_to_celsius(Temp_convert)
        print(f"{Temp_convert}°F is {temperature:.2f}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")