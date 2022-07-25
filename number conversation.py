
x=['Khan', 'Dhaka', '201-15-0000', 'DIU']
sum=0
count=[]
string = ''.join(x)
vowels = 'aeiouAEIOU'
for i in x:
    sum = sum + len(i)
final = [each for each in string if each in vowels]
print(len(final))
print(sum)
