user_input = input("Enter items separated by commas: ")
user_input1 = input("Enter items separated by commas: ")

original_list = user_input.split(',')
reversed_list = original_list[::-1]

original_list2 = user_input1.split(',')
reversed_list2 = original_list2[::-1]

print("Reversed list:", reversed_list)
print("Reversed list2:", reversed_list2)

numbers = [float(item.strip()) for item in reversed_list2 + reversed_list if item.strip().replace('.', '', 1).isdigit()]
characters = [item.strip() for item in reversed_list2 + reversed_list if not item.strip().replace('.', '', 1).isdigit()]

numbers.sort()
result = numbers + characters
print("Sorted numbers and added characters:", result)
