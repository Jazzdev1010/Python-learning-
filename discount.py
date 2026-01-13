age = int(input("Enter an Age:"))
is_member = input("Do you have a Membership?\nEnter True/False:")

if age >= 60:
    if is_member == "True":
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")