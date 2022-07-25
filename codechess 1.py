T=int(input())
A=list(map(int,input().strip().split()))[:T]
B=list(map(int,input().strip().split()))[:T]
X=list(map(int,input().strip().split()))[:T]
Y=list(map(int,input().strip().split()))[:T]
if A[0]*A[1]<=A[2]*A[3]:
    print("Yes")
else:
    print("No")
if B[0]*B[1]<=B[2]*B[3]:
    print("Yes")
else:
    print("No")

if X[0]*X[1]<=X[2]*X[3]:
    print("Yes")
else:
    print("No")

if Y[0]*Y[1]<=Y[2]*Y[3]:
    print("Yes")
else:
    print("No")
