a=input("enter a range")
n=input("enter a number")
count=0
for i in range(2,a):
    if n%i==0:
         count=count+1
         i=i+1
    else:
         count=count
if(count>1):
  print n
  print "is not a prime number"
else:
  print n,"is a prime"
 