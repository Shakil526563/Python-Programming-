ar=[]
n=int (input())
for i in range(n):
    row=[]
    for j in range(2):
        element=int (input())
        row.append(element)
ar.append(row)
for i  in range(n):
    for j in range(2):
    if ar[i][1]==ar[i][2]and ar[i + 1][1]==ar[i + 1][2]and ar[i + 2][1]==ar[i + 2][2]:
        print("Yes")
    else:
        print("No")

