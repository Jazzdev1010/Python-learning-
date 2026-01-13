string1=input("Enter a string:")
middle= len(string1)//2

if len(string1) > 0:
    print(f"First: {string1[0]}, Middle:{string1[middle]} Last: {string1[-1]}")
else:
    print("The string is empty.")