def add(a, b):
    result= a + b
    print("The sum of ", a, " and ", b, " is = ", result)

def sub(a, b):
    result = a - b
    print("The difference of ", a, " and ", b, " is = ", result)

def mult(a, b):
    result = a * b
    print("The product of ", a, " and ", b, " is = ", result)

def div(a, b):
    result = a / b
    print("The quotient of ", a, " and ", b, " is = ", result)

def mod(a, b):
    result = a % b
    print("The modulus result of ", a, " and ", b, " is = ", result)



print("Menu")
menu = ['1. Addition', '2. Subtraction', '3. Multiplication', '4. Division', '5. Modulus\n']
for x in menu:
    print("\t" + x)

retry = 1
print('\n')
while retry == 1:

    choice = int(input('Enter a number to choose your operation: '))

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print('\n')

    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mult(a, b)
    elif choice == 4:
        div(a, b)
    elif choice == 5:
        mod(a, b)
    else:
        print("Invlid Input")

    again = input("Would you like to do another calculation?(y/n): ")
    print('\n')

    if again == "y" or again == "Y":
        retry = 1
    elif again == "n" or again == "N":
        retry = 0

