
from pathlib import Path
from datetime import datetime
import sys


def mypath():
    with open("content.txt") as conn:
        for word in conn:
            print(word)

    connec = Path("content.txt").read_text()
    print(connec)


def main():
    try:
        year, month, day = list(
            input("date of birth seperated by a space(Year Month Day): ").split(" "))
        dt1 = datetime(int(year), int(month), int(day))
        start_year = int(year)
        leap = False
        leapyear = None
        while leap == False:
            if (start_year % 4) == 0:
                if (start_year % 100) == 0:
                    if (start_year % 400) == 0:
                        leap = True
                        leapyear = start_year
                    else:
                        start_year += 1
                else:
                    leap = True
                    leapyear = start_year
            else:
                start_year += 1
    except ValueError:
        print("Invalid year, month and day")
        print()
        main()
    except UnboundLocalError:
        print("invalid date of birth")
        print()
        main()
    dt2 = datetime.now()

    counter = 1
    while leapyear <= dt2.year:
        leapyear += 4
        counter += 1

    duration = dt2 - dt1
    years = int(duration.total_seconds() // (60 * 60 * 24 * 365))
    days = (int((int(duration.total_seconds()) %
                (60 * 60 * 24 * 365))/(60 * 60 * 24))) - counter
    print("{} Years and {} Days" .format(years, days))


password = "1234"
lenght = len(sys.argv)
if lenght == 2 and str(sys.argv[1]) == password:
    print("Welcome User!")
    main()
elif (lenght != 2):
    print("Only two command line argument is requred.")
else:
    print("Wrong password")
