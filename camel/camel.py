case = input("camelCase: ")

for i in case:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")
        
print()
