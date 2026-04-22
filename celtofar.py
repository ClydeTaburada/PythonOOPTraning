def cel_to_fahr(c):
    return (c * 1.8) + 32

temp = float(input("Enter Celsius: "))

print(cel_to_fahr(temp))