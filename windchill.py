
"""
Author: EKENEDO NZUBE EMMANUEL  

PURPOSE: The purpose of this project is to write a program that asks the user for a temperature
             and then shows the wind chill values for various wind speeds at that temperature. 
"""

#create a function that calculates the windchill

def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill

#create a function that getsthe user prefered input
def get_user_input():
    temperature = float(input("Enter the temperature: "))
    conversion = input("Enter the conversion type Celsius or Fahrenheit(C / F)): ")
    return temperature, conversion

#create a function that converts the temperaute type
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperature, conversion = get_user_input()

# Convert the temperature to Fahrenheit if necessary
if conversion.upper() == 'C':
    temperature = convert_to_fahrenheit(temperature)

# Display the wind chill values for various wind speeds
print("Wind Chill Values (in Fahrenheit) for Various Wind Speeds:")
print("--------------------------------------------------------")


for wind_speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print(f'At temperature {temperature}F, and wind speed {wind_speed}, the wind chill is: {wind_chill:.2f}F')