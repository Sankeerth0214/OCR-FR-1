a=raw_input("enter a input")
i=0
j=-1
count=0
for i in range(len(a)):
   if(a[i]==a[j]):
     count=count+1
     i=i+1
     j=j-1
   else:
     count=0
if(count>0):
  print a+"is a Polindrome"
else:
  print a+"is not a polindrome"