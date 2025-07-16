lines = []
print("Enter your text (press Enter on an empty line to finish):")

while True:
    line = input()
    if line == "":
        break

    clean_text = line.rstrip()
    print(clean_text)

    lines.append(clean_text)
