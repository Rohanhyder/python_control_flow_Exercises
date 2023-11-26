
# get the year from the user.

year = int(input("Enter a year "))

# check the year is leap year or not.

if year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
