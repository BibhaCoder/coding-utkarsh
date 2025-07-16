word1 = input("Type the first string: ")
word2 = input("Type the second string: ")

if word1 == word2:
    print("These are the same!")
else:
    close = True
    i = 0

    while i < len(word1) and i < len(word2):
        letter1 = word1[i]
        letter2 = word2[i]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        pos1 = 0
        pos2 = 0

        while alphabet[pos1] != letter1:
            pos1 += 1
        while alphabet[pos2] != letter2:
            pos2 += 1

        if pos1 > pos2 + 1 or pos2 > pos1 + 1:
            close = False
            break

        i += 1

    if close:
        print("The words are pretty close ngl...")
    else:
        print("The words are far apart fr ngl but gl")
