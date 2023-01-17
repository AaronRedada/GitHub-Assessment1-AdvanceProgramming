staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Anmol","Zainab","Iftikhar", "Arshiya","Jake","Iftikhar"]

print("Choose a number associated with the name and it will show how many times it appears in the list:")
print("1 - Arshiya")
print("2 - Usman")
print("3 - Iftikhar")
print("4 - Anmol")
print("5 - Zainab")
print("6 - Jake\n")

def name_count(x):
    if x == 1:
        count = staff.count("Arshiya")
        print("\nThe amount of times Arshiya appears in the list is:", count)
    elif x == 2:
        count = staff.count("Usman")
        print("\nThe amount of times Usman appears in the list is:", count)
    elif x == 3:
        count = staff.count("Iftikhar")
        print("\nThe amount of times Iftikhar appears in the list is:", count)
    elif x == 4:
        count = staff.count("Anmol")
        print("\nThe amount of times Anmol appears in the list is:", count)
    elif x == 5:
        count = staff.count("Zainab")
        print("\nThe amount of times Zainab appears in the list is:", count)
    elif x == 6:
        count = staff.count("Jake")
        print("\nThe amount of times Jake appears in the list is:", count)
    

name = int(input("Enter the number of the name you have chosen: "))

print(name_count(name))

