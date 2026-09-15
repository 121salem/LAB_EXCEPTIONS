def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        try:

            user_input = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
            parts = user_input.strip().split()
            
            if len(parts) != 2:
                raise ValueError("Invalid format. Please enter temperature and unit separated by a space.")
            
            temp_str, unit = parts
            temp_val = float(temp_str)

            if unit.upper() == 'C':
                converted = celsius_to_fahrenheit(temp_val)
                print(f"Temperature in Fahrenheit: {converted} F")
                break
            elif unit.upper() == 'F':
                converted = fahrenheit_to_celsius(temp_val)
                print(f"Temperature in Celsius: {converted} C")
                break
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError as e:
            print(f"Invalid temperature value. Please try again.")
        except TypeError as e:
            print(f"Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()