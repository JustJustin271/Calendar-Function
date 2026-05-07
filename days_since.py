accum_list = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

'''
the_list= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

accum_list = []
total = 0

for i in the_list:
    total += i
    
    accum_list.append(total)

print(accum_list)
'''

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        

def day_count(date):
    month = date.month
    day = date.day
    year = date.year
    
    year = (year * 365) + year//4 - year//100 + year//400
    month = accum_list[month - 1]
    
    days_counted = year + month + day
    
    return days_counted
    
print("=== First date information ===")
m1 = int(input("Enter a month (1-12): "))
d1 = int(input("Enter a day of the month (1 - 31): "))
y1 = int(input("Enter a year (ie. 2026): "))

print("\n=== Second date information ===")
m2 = int(input("Enter a month (1-12): "))
d2 = int(input("Enter a day of the month (1 - 31): "))
y2 = int(input("Enter a year (ie. 2026): "))

first_date = Date(m1, d1, y1)
second_date = Date(m2, d2, y2)

first_days = day_count(first_date)
second_days = day_count(second_date)

day_differ = second_days - first_days

print("\n\nI recommend not including the last date")
print("If do, the difference between Jan 1 & Jan 2nd")
print("Is now a difference of 2 days if you do include it :)\n")
choice = input("\nInclusive of the last day? (y/n): ").lower().strip()

if "y" in choice:
    day_differ += 1

print("\n=== Calculation ===")
print(f"Difference between dates is {day_differ} days")

# Days since calculator
# Created and edited on May 6th, 2026 :)
# It's purpose is to find the number of days between 2 dates :D
