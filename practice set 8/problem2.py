# c/5=(f-32)/9

def fahrenheitToCelsius(f):
    c=5*((f-32)/9)
    return c

f=int(input("Enter temperature in Fahrenheit: "))
c=fahrenheitToCelsius(f)
print(f"Temperature in Celsius is: {c}")




def celsiusToFahrenheit(c):
    f=(c*9/5)+32
    return f

c=int(input("Enter temperature in Celsius: "))
f=celsiusToFahrenheit(c)
print(f"Temperature in Fahrenheit is: {f}")