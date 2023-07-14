user = input("expressions: ")

x,y,z = user.split(" ")

x1 = float(x)
z1 = float(z)

if y == "+":
    value = x1 + z1

elif y == "/":
    value = x1 / z1

elif y == "-":
    value = x1 - z1

else:
    value = x1 * z1

print(value)