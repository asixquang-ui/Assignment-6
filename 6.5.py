def remove_odd(numbers):
    new_list = []

    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)

    return new_list


# main program
original_list = [1, 2, 3, 4, 5, 6, 7, 8]

result = remove_odd(original_list)

print("Original list:", original_list)
print("List without odd numbers:", result)