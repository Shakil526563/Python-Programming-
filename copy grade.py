sum=0
count=0
grade=int(input("Enter the mark if u enter -1 then end: "))
while grade!=-1:
    sum=sum+grade
    count=count+1
    grade = int(input("Enter the mark if u enter -1 then end: "))
if count!=0:
    avg=sum/count
    print("averge ",'%.2f'%(avg))
else:
  print("There is no value enter")

