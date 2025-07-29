i = int(input("Enter a number: ")) 
string = ""
while i != 0:
    r = i % 10
    i = i // 10
    string = str(r) + string  
print(string)
