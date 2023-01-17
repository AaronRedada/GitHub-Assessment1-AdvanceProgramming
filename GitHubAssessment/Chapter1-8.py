num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))

print(num1, " is the largest number") if (num1 > num2 and num1 > num3) else print(num2, " is the largest number") if (num2 > num1 & num2 > num3) else print(num3, " is the largest number") if (num3 > num1 and num3 > num2) else print("None are larger than the other")