x=['Khan', 'Dhaka', '201-15-0000', 'DIU']
string=''.join(x)
vowel='aeiouAEIOU'
sum=0
cont=0
for i in x:

 print(len(i))
v=[i for i in string if i in vowel]
print(len(v))
c=[i for i in string]

print(len(c))