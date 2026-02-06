numbers = [10, 20, 30, 40, 50]
target = 30

found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")
