n=int(input("Enter the initial number : "))
y=int(input("Enter the last number : "))
for i in range(n,y+1):
    if i>1:
        for num in range(2,i):
            if (i%num)==0:

                break
        else:
            print(i)

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)