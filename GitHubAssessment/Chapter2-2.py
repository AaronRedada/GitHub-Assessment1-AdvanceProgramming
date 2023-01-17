list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Here are all of the items in the list: ")
for x in list:
    print(x)

print("\nThe largest number in the list is: ", max(list))
print("The lowest number in the list is: ", min(list), "\n")

list.sort()
print("Ascending Order:", list)

list.sort(reverse=True)
print("Descending Order:", list)

add1 = int(input("\nEnter a number: "))
list.append(add1)
add2 = int(input("Enter a 2nd number: "))
list.append(add2)

print("\nHere is the updated list:", list)




