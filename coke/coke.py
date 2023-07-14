coke = 50

while coke > 0:
    print("Amount Due:",coke)
    coin = int(input("Insert coin: "))

    if coin in [5, 10, 25]:
        coke = coke - coin

print("change owed:",abs(coke))