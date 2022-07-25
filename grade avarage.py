totall=0
gradecount=0
grade=int(input("Enter grade :"))
while grade!=-1:
    totall=totall+grade
    gradecount=gradecount+1
    grade=int(input("enter grade:"))

if gradecount!=0:
    avg=totall/gradecount
    print(avg)
else:
    print("grade are not invaid")
