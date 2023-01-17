#Take input from user and assign it to variables
name = input("What is your Name? ")
age = input("What is your Age? ")
ht = input("Where is your Hometown? ")
 
#Open the text.txt file for appending.
 
file1 = open('bio.txt', 'w')
 
#Write the content of the variables to the text.txt file
file1.write(name)
file1.write("\n")
file1.write(age)
file1.write("\n")
file1.write(ht)
file1.write("\n")
 
#Close the text.txt file
file1.close()