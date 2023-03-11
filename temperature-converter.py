def convert_temperature(temperature, from_unit, to_unit):
    # convert temperature to Kelvin
    if from_unit == 'Celsius':
        temperature_k = temperature + 273.15
    elif from_unit == 'Fahrenheit':
        temperature_k = (temperature + 459.67) * 5/9
    elif from_unit == 'Rankine':
        temperature_k = temperature * 5/9
    else: # assume input is already in Kelvin
        temperature_k = temperature

    # convert temperature from Kelvin to desired unit
    if to_unit == 'Celsius':
        temperature_conv = temperature_k - 273.15
    elif to_unit == 'Fahrenheit':
        temperature_conv = temperature_k * 9/5 - 459.67
    elif to_unit == 'Rankine':
        temperature_conv = temperature_k * 9/5
    else: # assume output is in Kelvin
        temperature_conv = temperature_k

    return temperature_conv
temp = float(input('temperature: '))
intialUnit = input('from: ')
newUnit = input('to: ')
print(convert_temperature(temp, intialUnit, newUnit))