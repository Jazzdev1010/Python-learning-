username = input("Enter your Username: ")

length = len(username) >= 6

def valid_user(username):
    if (
        length and
        username[0].isalpha() and
        username[-1].isdigit()
    ):
        print("Username is Valid")
    else:
        print("Username is Invalid")

valid_user(username)