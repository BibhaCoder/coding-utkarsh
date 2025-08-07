a = input()
array = []
for char in a:
    array.append(char)
for i in range(len(array)-1, -1, -1):
    print(array[i])
