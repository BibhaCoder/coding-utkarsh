lines = []
print("Enter your text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    if len(line) > 80:
        lines.append(line)

for line in lines:
    print("Long line found:")
    print(line)
else:
  print ("Nothing")
