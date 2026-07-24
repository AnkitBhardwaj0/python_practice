def login_required(function):
    def wrapper():
        print("Checking login...")
        function()
    return wrapper
@login_required
def profile():
    print("Welcome to your profile.")

profile()