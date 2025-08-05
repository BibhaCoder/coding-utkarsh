def atoi():
  a = input()
  i = 0
  sign = 1
  print(a)
  number = 0
  if a[0] == "+":
    i += 1
  if a[0] == "-":
      sign = -1
      i += 1
  while i < len(a):
    number = number * 10 + int(a[i])
    i += 1
  print(number)
  print(number * sign)
atoi()
