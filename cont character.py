
x=['Khan', 'Dhaka', '201-15-0000', 'DIU']
sum=0
count=[]
string = ''.join(x)
vowels = 'aeiouAEIOU'
digit='1234567890'
sp='-'
for i in x:
    sum = sum + len(i)
final = [each for each in string if each in vowels]
digite = [each for each in string if each in digit]


print(len(sp))
print(len(digite))
print(len(final))
print(sum)

str='shakil is good boy'
st=str.capitalize()
print(st)

set={1,2,5}
s={6,5}
set.update(s)
print(set)
print(st)
