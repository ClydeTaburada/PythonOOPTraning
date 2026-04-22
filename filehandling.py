try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File does not exist.")
finally:
    print("Done reading file")