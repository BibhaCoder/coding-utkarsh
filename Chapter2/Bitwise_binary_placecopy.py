def setbites():
    x = int(input("Enter binary value: "))
    p = int(input("Enter position: "))
    n = int(input("Enter binary length: "))
    print (bin(x))
    x = bin(x)[2:]
    print ("IGNORE FIRST NUMBER")


    print(x[-(p + 1)])

    i = 0
    while i < n:
        print(x[-(p + 1 + i)])
        i += 1

setbites()
