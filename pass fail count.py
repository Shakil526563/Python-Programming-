
pas=0
fail=0
for i in range(10):
    n=int(input("If you pass the exam then click 1,otherwise 2:"))
    if n==1:
        pas=pas+1
    elif n==2:
        fail=fail+1
print(pas)
print(fail)
if pas>8:
    print("Bonous instractor")
