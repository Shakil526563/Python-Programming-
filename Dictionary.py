n = int(input("enter a number of elements in the dict: "))
my_dict = {}
for i in range(n):
    key = input("Enter key :")
    value = input("Enter values :")
    my_dict.update({key: value})
print(my_dict)

"""myDict = {'one': 'Sally', 'two': 13, 'three': 'Dingra', 'four': 'Lilop'}
myDict.update({'two':'Billy'})
print(myDict)
myDict = {'one': 'Sally', 'two': 13, 'three': 'Dingra', 'four': 'Lilop'}
myDict.pop('two')
print(myDict)"""