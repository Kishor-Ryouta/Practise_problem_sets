def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO - just remove the dollar sign
    dollar = d.replace("$"," ")
    return float(dollar)


def percent_to_float(p):
    # TODO - just remove the % sign
    percentage = int(p.replace("%"," ")) / 100
    return float(percentage)


main()