# mario in python

from cs50 import get_int

# force input between 1 and 8
while True:
    Height = get_int("Height: ")
    if Height >= 1 and Height <= 8:
        break

for i in range(0,Height):
    for j in range(0, Height):
        if i+j < Height-1:
            print(" ",end="")
        else:
            print('#',end="")
    print("  ",end="")
    for k in range(0,i+1):
        print('#',end="") 
    print(' ')


