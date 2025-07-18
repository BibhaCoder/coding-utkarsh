
F = list(range(-100, 100)) 
C = list(range(-100, 100))
i = 0
for item in F:
  C[i] = (F[i] - 32) * (5/9)
  i += 1
print i
i = 0
for item in F:
  print (F[i], C[i])
  i += 1
  
