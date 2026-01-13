username = input("Enter your Username: ")

def valid_user(username):
    valid = True

    if len(username) < 6:
        print("Username length must be at least 6")
        valid = False

    if not username[0].isalpha():
        print("First character must be a letter")
        valid = False

    if not username[-1].isdigit():
        print("Last character must be a digit")
        valid = False

    if valid:
        print("Valid Username")
    else:
        print("Invalid Username")

valid_user(username)
