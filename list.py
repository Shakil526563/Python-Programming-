number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)


list=['shakil',7,'ss','cse']
print(list)
print(list[-1])
print('shakil' in list)

if True:
    print(list)
print('shakil' not in list)
print(list[:1])
print(list[1])
list[2]='shakil rana'
for i in range(len(list)):
    if list[i]=='ss':
        list[i]='munna'

print(list)
print(list)

del list[-1]
print(list)

list.extend(['shjka',2])
print(list)

list.insert(3,'munna')
print(list)

for i in range(1,10,2):
    print(i)

list=[2,5,89,4]

print(list.index(89))
