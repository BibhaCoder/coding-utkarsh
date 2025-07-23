def setbits():
  x = int(input("Enter x:"))
  p = int(input("Enter p:"))
  n = int(input("Enter n:"))
  y = int(input("Enter y:"))
  y_mask = ~(~0 << int(n))
  print bin(y)
  print bin(y_mask)
  y &= y_mask
  print bin(y)
  x_mask = (~(~0 << n)) << (p + 1 - n) 
  x = x & (~x_mask)
  x = x | (y << (p + 1 - n))
  print bin(x)
  
  
setbits()
