#Converting Temperature Celsius into Fahrenheit 
celsius = float(input("Enter the celcius: "))
def convertTemperature(celcius):
    fahrenheit= (celcius * 9/5) + 32
    return fahrenheit
fahrenheit = convertTemperature(celsius)
print(celsius,"Celsius =",fahrenheit,"Fahrenheit")
