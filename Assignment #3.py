"""Python program for converting temperature from Fahrenheit to Celsius and vice versa"""
def CelsiustoFahrenheit(celsius):
    fahrenheit=(9/5)*celsius+32
    return fahrenheit

def FahrenheittoCelsius(fahrenheit):
    celcius=(5/9)*(fahrenheit-32)
    return celcius

if __name__=="__main__":
    print("Temperature converter pro\nThese are the available temperature conversions:\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius")
    menu = input("Please input 1 or 2 to select corresponding conversion: ")
    if menu == "1":
        x = input("input temperature in Celsius: ")
        c2f=round(CelsiustoFahrenheit(float(x)),2)
        print("{} C = {} F" .format(x,c2f))
    if menu == "2":
        x = input("input temperature Fahrenheit: ")
        f2c=round(FahrenheittoCelsius(float(x)),2)
        print("{} F = {} C" .format(x,f2c))

