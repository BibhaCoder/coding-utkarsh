a = input("Enter first string: ")
b = input("Enter second string: ")

if len(a) != len(b):
    print("Not 1 away (different lengths)")
    quit()

diff = 0
for i in range(len(a)):
    if a[i] != b[i]:
        diff += 1

print("diff is " + str(diff))

if diff == 1:
    print("1 away")
else:
    print("Not away")
