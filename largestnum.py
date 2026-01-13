a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
c = int(input("Enter third Number: "))

if a >= b:
    if a >= c:
        print("Largest Number:", a)
    else:
        print("Largest Number:", c)
else:
    if b >= c:
        print("Largest Number:", b)
    else:
        print("Largest Number:", c)
