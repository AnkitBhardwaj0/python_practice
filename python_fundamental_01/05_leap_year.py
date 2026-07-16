#Check whether a year is a leap year.
def leap_year(year):
    if year%4==0:
        return True
    else:
        return False
print(leap_year(2001))
print(leap_year(2004))