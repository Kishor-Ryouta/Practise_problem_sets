#program to convert 12hrs to 24hrs time format

import re

def main():
    #Enter the 12hrs time format
    print(convert(input("Hours: ")))


def convert(s):
    #re for the following formats:
        #9:00 AM to 5:00 PM
        #9 AM to 5 PM
    if time := re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s):
        group = time.groups()
        # raise error if not in 12hrs format
        if int(group[1]) > 12 or int(group[5]) > 12:
            raise ValueError
        group1 = time_format(group[1], group[2], group[3])
        group2 = time_format(group[5], group[6], group[7])
        return f"{group1} to {group2}"
    else:
        raise ValueError

def time_format(hour, minute, meridiem):
    # convert 12hrs to 24hrs format on PM
    if meridiem == "PM":
        if int(hour) == 12:
            hour_new = 12
        else:
            hour_new = int(hour) + 12

    elif int(hour) == 12:
        hour_new = 0
    else:
        hour_new = int(hour)

    #replace 'None' with '00'
    if minute == None:
        minute_new = "00"
        time_new = f"{hour_new:02}:{minute_new}"
    elif int(minute) > 59:
        raise ValueError
    else:
        time_new = f"{hour_new:02}:{minute}"

    return time_new

if __name__ == "__main__":
    main()