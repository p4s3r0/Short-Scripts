# First Semester -> 2018
# -------------------------------------------------------------------
# Lets calculate something. The weekday of January first from the year you are born.
# Carl Friedrich GauS (born 1777) invented following formula and was able to calculate every weekday of a given year
# by calculating following formula we get a number between 0 and 6
# (1 + 5 * ((year - 1) MODULO 4) + 4 * ((year - 1) MODULO 100) + 6 * ((year - 1) MODULO 400)) MODULO 7
# if it is 0, the day was a Sunday, if it is 1, the day was a Monday, ..., if it is 6, the day was a Saturday
#Pasero Christian
while 1:
    try:
        year = int(input("Year: "))
        formula = (1 + 5 * ((year - 1) % 4) + 4 * ((year - 1) % 100) + 6 * ((year - 1) % 400)) % 7

        if formula == 1:
            day = "Monday"
        elif formula == 2:
            day = "Tuesday"
        elif formula == 3:
            day = "Wednesday"
        elif formula == 4:
            day = "Thursday"
        elif formula == 5:
            day = "Friday"
        elif formula == 6:
            day = "Saturday"
        else:
            day = "Sunday"

        print("1. January", year, "was a", day)

    except ValueError:
        print("Gib ein gueltiges Jahr ein")
