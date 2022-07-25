

word=0
digit=0
letter=0
x=input()
for n in x:
 n.lower()
 if n==" ":
   word=word+1

 elif n>'0' and n<='9':
    digit=digit+1
 elif n>='a' and n<='z':
    letter=letter+1
print(word+1)
print(digit)
print(letter)