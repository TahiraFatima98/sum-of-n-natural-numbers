print("sum of n natural numbers:")
n=int(input("Enter a number" "\n"))
sum=0
if(n<=0):
    print("Enter a positive number.")
else:
    while(n>0):
        sum=sum+n
        n=n-1
print("sum=" + str(sum))
