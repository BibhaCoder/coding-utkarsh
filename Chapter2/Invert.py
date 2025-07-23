def invert():
  x = int(input("Enter x:"))
  p = int(input("Enter p:"))
  n = int(input("Enter n:"))
  
  
  
  
  print ("x before invert")
  print bin(x)
  x_mask = (~(~0 << n)) << (p + 1 - n)
  print bin(x_mask)
  x = x  ^ (x_mask)
  print ("x after invert")
  print bin(x)
  

  
  
invert()
