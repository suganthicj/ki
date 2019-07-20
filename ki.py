X1,Y1=map(int,input().split())
for a in range (X1+1,Y1):
  for b in range (2,a):
    if (a%b==0):
      break
  else:
      print(a,end=" ")
