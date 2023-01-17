print("Printing each line in text file")

with open("numbers.txt") as file_handler:
   	lines = file_handler.read()
    print(lines)

