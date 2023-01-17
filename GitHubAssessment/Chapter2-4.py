year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

print(year[-3], "\n")

print("Original Order: ", year)
def reverse(t):
    new_tuple = ()
    for i in range(len(t)-1, -1, -1):
        new_tuple += (t[i],)
    return new_tuple
 
print("Reversed Order: ", reverse(year), "\n")

nine = year.count(2009)

print("The number of times 2009 is on the list is: ", nine)
print("The index value of 2018 is: ", year.index(2018))
print("The length of the tuple is: ", len(year))
