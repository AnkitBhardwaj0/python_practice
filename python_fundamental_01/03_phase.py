"""
Take a person's age and print:
Child (0-12)
Teenager (13-9)
Adult (20-59)
Senior Citizen (60+)
"""
def person(age):
    if age in range (0,13):
        print("child")
    elif age in range (13,20):
        print("teenager")
    elif age in range (20,60):
        print("adult")
    elif age in range (60,150):
        print("senior citizen")
    else:
        print("invalid input")

person(9)
person(13)
person(59)
person("s")
person(60)
person(61)