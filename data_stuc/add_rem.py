letters = ["a", "b", "c"]
# Add
letters.append("b")
print(letters)
letters.insert(0, ":")
print(letters)

# Remove
letters.pop(0)
letters.remove("b")
print(letters)
del letters[0:2]
letters.clear()
print(letters)
