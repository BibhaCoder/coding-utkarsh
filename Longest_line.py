
lines = []
print("Enter your text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)


i = 0
longest_line = ""
longest_length = 0
for element in lines:
  if len(lines[i]) > longest_length:
    longest_length = len(lines[i])
    longest_line = lines[i]
  i += 1
print ("Longest line=" + longest_line)
