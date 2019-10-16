letters = ["a", "b", "c", "d", "b"]
for letter in range(letters.count("b")):
    letters.remove("b")
print(letters)
