def invert():
    x = int(input("Enter value: "))
    p = int(input("Enter position: "))
    n = int(input("Enter bits to be converted: "))

    if n > p + 1:
     print("Invalid n" + str(n))
     return
    mask = ((1 << n) - 1) << ( p + 1 - n)
    result = x ^ mask
    print (bin(x) + "    <---this changed into this --->  " + bin(result))



invert()
