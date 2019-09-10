command = ""
while command.lower() != "quit":
    command = input(">")
    print("Output", command)

while True:
    command = input(">")
    print("Output", command)
    if command.lower() == "quit":
        break
