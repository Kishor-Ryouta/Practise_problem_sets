# Bitcoin program
import sys
import requests

#amount of bit coins the user wants to buy
if len(sys.argv) == 2:
    try:
        x = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command line argument")

#print the total amount the user has to pay in "$"
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    bitcoin = r["bpi"]["USD"]["rate_float"]
    amount = float(sys.argv[1]) * bitcoin
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("An Error Occured")
    sys.exit(1)