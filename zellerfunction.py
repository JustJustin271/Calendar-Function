days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

month_names = ["", "January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

def zeller(date):
    month = date.month
    day = date.day
    year = date.year

    
    if month < 3:
        year -= 1
        month += 12

    k = year % 100
    j = year//100

    h = ((
    day +
    (13 * (month + 1))//5 +
    k +
    k//4 +
    j//4 -
    2* j) %7)
    return h

def day_of_week(date):
    return days[zeller(date)]

orange = Date(1, 1, 1970)

assert day_of_week(Date(1, 1, 1970)) == "Thursday"
assert day_of_week(Date(10, 20, 2010)) == "Wednesday"
assert day_of_week(Date(10, 1, 2011)) == "Saturday"
assert day_of_week(Date(5, 6, 2011)) == "Friday"
print("All tests passed!\n\n")

m = int(input("Enter a month (1-12): \n"))
d = int(input("\nEnter a day of the month (1 - 31): \n"))
y = int(input("\nEnter a year (ie. 2026): \n"))

custom_date = Date(m, d, y)

day_name = day_of_week(custom_date)

print(
    f"\nYour date is: \n{day_name}, "
    f"{month_names[custom_date.month]} {custom_date.day},"
    f" {custom_date.year}")

# This is the remake of the Zeller Function from Dr. Racket
# It is a a whole lot simplier and doesn't need let* :D
# Created April 17th, 2026
# Last Edited: April 24th, 2026
