num = int(input("Enter a number: ")) 
base = int(input("Enter base value: ")) 
string = ""
while num != 0:
    r = num % base
    num = num // base
    string = str(r) + string  
print(string)
