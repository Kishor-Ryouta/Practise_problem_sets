from datetime import datetime, date
import sys
import inflect

p = inflect.engine()

def get_date(birth):
    #obtain today's date in string format
    #today = '2000-01-01'
    today = datetime.strftime(date.today(), '%Y-%m-%d')
    date1 = date.fromisoformat(today)
    date2 = date.fromisoformat(birth)
    difference = abs((date1 - date2).days)
    return difference

def get_minutes(difference):
    return difference*24*60

def get_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return words



def main():
    #user input in the format of 'YYY-MM-DD'
    birth = input("DOB (YYYY-MM-DD): ")
    #exit program if not in the specified format
    try:
        datetime.strptime(birth, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid date")


    #get the age of the person or the difference between the dates in general.
    difference = get_date(birth)

    #convert years into minutes
    minutes = get_minutes(difference)

    #print the difference in words
    words = get_words(minutes)
    print(words.capitalize() + " " + "minutes")

if __name__ == "__main__":
    main()