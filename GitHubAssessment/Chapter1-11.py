count = 0

while count < 100:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
else:
    print("Loop Terminated")