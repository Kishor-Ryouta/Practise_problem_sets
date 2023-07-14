import math

while True:
    fuel = input("Enter the fraction: ")

    try:
        x,y = fuel.split("/")

        x1 = int(x)
        y1 = int(y)

        f = (x1/y1)

        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

f = round(f * 100)

if f >= 99:
    print("F")
elif f <= 1:
    print("E")
else:
    print(f"{f}%")

