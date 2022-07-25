dele = []
string = input("Enter any string: ")
ele = ('a', 'e', 'i', 'o', 'u')
newstr = []
for x in string.lower():
    if x in ele:
        dele.append(x)
        newstr=string.replace(x,"")

print(f'new string :{newstr} from {string}')
print(f'delete {dele}')