str = input("Enter a number: ")
i = 0
num = 0
for char in str: 
  num = num  * 10 + int(str[i])
  i += 1
print num
