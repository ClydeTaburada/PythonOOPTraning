def odd_even(c):
    if c % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

c = int(input("Enter Number: "))

print(odd_even(c))  