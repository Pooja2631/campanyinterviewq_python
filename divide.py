def Divide(D,E):
  R = D
  i = 0


  while R >= E:
    R = R - E
    i += 1

  return i

D = int(input("enter the number..."))
E = int(input("enter the number.."))
print("Quotient : ",Divide(D,E))