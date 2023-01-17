count = 0
ans = 0

while ans < 1:
    answer = input("Would you like to continue? (y/n): ")
    if answer in ['y', 'Y']:
        count = count + 1
    else:
        ans = ans + 1

print(count, " is how many times you continued.y")
