def calc_square(x):
    result = x ** 2
    print("The area of the square is: ", result)

def calc_triangle(x, y):
    result = (x * y) * 0.5
    print("The area of the triangle is: ", result)

def calc_circle(x):
    result = (x ** 2) * 3.1416
    print("The area of the circle is: ", result)

print("Choose a number correspoing to what you want to calculate:")
print("1: Calculate the area of a square", "\n2: Calculate the area of a circle", "\n3: Calculate the area of a triangle")
choice = int(input("\nEnter the number of your choice: "))
print('\n')

if choice == 1:
    side = int(input("Enter the value of the side of the square: "))
    print('\n')
    calc_square(side)
elif choice == 2:
    radius = int(input("Enter the radius of the circle: "))
    print('\n')
    calc_circle(radius)
elif choice == 3:
    height = int(input("Enter the height of the triangle: "))
    base = int(input("Enter the base of the triangle: "))
    print('\n')
    calc_triangle(height, base)
else:
    print("INVALID INPUT")
