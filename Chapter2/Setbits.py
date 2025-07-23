def setbits():
  x = int(input("Enter x:"))
  p = int(input("Enter p:"))
  n = int(input("Enter n:"))
  y = int(input("Enter y:"))
  mask = ~(~0 << int(n))
  print bin(y)
  print bin(mask)
  y &= mask
  print bin(y)
  
  
  
setbits()
  
