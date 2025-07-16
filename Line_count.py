
lines = []
print("Enter your text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = "\n".join(lines)
print("You entered this much lines:")
print (str(len(lines)))
