l = input("Enter the string: ")
s = input("Enter the substring: ")

print("Count:", l.count(s))

count = 0
while count <= len(l) - len(s):
  if l[count:count+len(s)] == s:
    print("1")
    print("First position:", count)
    quit()
  count += 1

print("First position: -1")
