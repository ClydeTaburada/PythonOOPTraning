def get_largest_num(x,y,z,a,b):
    return max(x,y,z,a,b)

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))
num4 = int(input("Enter 4th Number:"))
num5 = int(input("Enter 5th Number:"))

print("The largest number is:" , get_largest_num(num1,num2,num3,num4,num5))