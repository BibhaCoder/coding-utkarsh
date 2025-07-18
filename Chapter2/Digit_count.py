a = input("Enter your input: ")

char_count = 0
num_count = 0
digit_usage = [0] * 10
letter_usage = [0] * 26  # For a–z

for char in a.lower():
    if char.isdigit():
        num_count = num_count + 1
        digit_usage[int(char)] = digit_usage[int(char)] + 1
    elif char.isalpha():
        char_count = char_count + 1
        index = ord(char) - ord('a')
        if index >= 0 and index < 26:
            letter_usage[index] = letter_usage[index] + 1

print("Characters: " + str(char_count))
print("Numbers: " + str(num_count))

print("\nDigit usage (0–9):")
for i in range(10):
    print(str(i) + ": " + str(digit_usage[i]) + " time(s)")
print("\nLetter usage (a–z):")
for i in range(26):
    print(chr(i + ord('a')) + ": " + str(letter_usage[i]) + " time(s)")
