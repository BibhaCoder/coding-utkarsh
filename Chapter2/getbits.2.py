def setbites():
    x = int(input("Enter binary value: "))
    p = int(input("Enter position: "))
    n = int(input("Enter binary length: "))
    print (bin(x))
    if n > p + 1:
     print("Invalid n" + str(n))
     return
    mask = (~(~0 << n))
    y = (x >> (p + 1 - n) & mask)
    print (bin(y))


setbites()
