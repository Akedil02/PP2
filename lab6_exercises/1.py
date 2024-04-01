def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5]
result = multiply_numbers(my_list)
print("Multiple of all numbers in the list:", result)
