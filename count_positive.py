list_num = [1, 4, 3, 7, 8, 10, 2, 14, 9]

def count_positive(list_num):
    count_even = 0
    for num in list_num:
        if num % 2 == 0:
            count_even += 1
    return count_even

print(count_positive(list_num))