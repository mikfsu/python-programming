def multiply(*numbers):
    total = 1
    for number in numbers:
        print(number)
        total = total*number
    return total


print(multiply(3, 4, 5, 6))
