def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total*number
    return total


print("Start")
print(multiply(3, 4, 5, 6))
