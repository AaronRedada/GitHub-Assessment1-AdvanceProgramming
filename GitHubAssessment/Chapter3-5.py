def product(list):
    result = 1
    for x in list:
        result = result * x

    print("The product of everything in the list is: ", result)


list = [1, 2, 3, 4, 5]
product(list)