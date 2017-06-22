n=input("enter a number")
count=0
if n%2!=0:
    count=count+1
else:
    count=0
if(count>0):
  print n
  print "is not an even number"
else:
  print n,"is an even number"