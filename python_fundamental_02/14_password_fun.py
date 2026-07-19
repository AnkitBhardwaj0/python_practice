#Validate a password with functions.
def password_checker(password):
    if len(password)<8:
        print("password must have 8 digit or more")
    elif not any(ch.islower() for ch in password):
        print("password must contain at least one lowercase letter")
    elif not any(ch.isupper() for ch in password):
        print("password must contain at least one uppercase letter")
    elif not any(ch.isdigit() for ch in password):
        print("password must contain at least one digit ")        
    elif not any(not ch.isalnum() for ch in password):
        print("passord must contain at least one special character")
    else:
        print("set password sucessfully")
        return True

while True:
    password=input("enter password")
    check=password_checker(password)
    if check:
        break