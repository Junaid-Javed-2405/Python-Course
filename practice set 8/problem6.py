def inchesToCm(inches):
    cm=inches*2.54
    return cm

n=int(input("Enter the length in inches: "))
print(f"{n} inches is equal to {inchesToCm(n)} cm")