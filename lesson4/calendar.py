year = int(input("Enter year in format (YYYY):"))
if year <= 1900 or year >= 1_000_000:
    print("Year not match requirements!")
else:
    if year % 4 > 0 and year % 100 > 0 or year % 400 > 0:
        print("Year is not leap")
    else:
        print("Year is leap")
