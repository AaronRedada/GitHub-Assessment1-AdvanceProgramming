print("-Enter the three sides of the triangle-")
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

def triangle(a):
    if side3 >= (side1 + side2):
        print("\nThis is a triangle")
    else:
        print("\nThis is not a triangle")

print(triangle(1))
