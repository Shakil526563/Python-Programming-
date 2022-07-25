c=(1,2,3,4,5)
d=(4,5,6,7,8)
e=(3,6,9,2,5)
f=(8,2,5,8,7)
tm1=c+d
tm2=e+f
print(tm1)
print(tm2)
tm=list(tm1)
tm.pop()

tm3=list(tm2)
tm3.pop()


print(tm)
print(tm2)

tm.insert(6,10)

print(tm)
tm3.insert(6,12)
print(tm3)