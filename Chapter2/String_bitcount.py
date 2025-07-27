x = input("Enter binary string: ")
count = 0
for num in x:
    print(num)
    if num == '1':
        count += 1
print("Number of 1's:", count)
