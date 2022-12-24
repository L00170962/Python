"""
Script : kelvin_to_F_and_C.py
By : AV
Purpose : To demonstarte with the help of for loop convert kelvin temp to Celsius and Fahrenheit

"""
# Kelvin temperatures in list
kelvin_temp = [293, 297, 259, 500, 235, 310.15, 321, 342, 333,421]

# Doing kelvin to ferenheit conversion on the go with for loop
temp_in_faren = [(1.8 * (temp - 273) + 32) for temp in kelvin_temp]

# Doing kelvin to celcius conversion on the go with for loop
temp_in_celcius = [(temp- 273.15) for temp in kelvin_temp]

#Print results in faren and celcius after formatting
output_fahren = ['{:.2f}F'.format(val) for val in temp_in_faren]
output_celcius = ['{:.2f}C'.format(val) for val in temp_in_celcius]
print(*output_fahren, sep= ', ')
print(*output_celcius, sep=', ')

