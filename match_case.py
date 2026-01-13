number = int(input("Enter a Num:"))

match number:
    case 4:
        print("Four")
    case 5 | 6:
        print("five or Six")
    case _:
        print("Other number")