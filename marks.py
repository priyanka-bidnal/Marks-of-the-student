import sys
if len(sys.argv)==5:
  n1=sys.argv[0]
  n2=sys.argv[1]
  n3=sys.argv[2]
  n4=sys.argv[3]
  n5=sys.argv[4]
else:
  n1=80
  n2=60
  n3=70
  n4=50
  n5=90
avg=(n1+n2+n3+n4+n5)/5
print("Average marks:",avg)
if(avg>=100):
    grade="A"
if(avg>=80):
    grade="B"
if(avg>=60):
    grade="C"
if(avg>=40):
    grade="D"
else:
    grade="Fail"
print("Grade=",grade)     
  
  
