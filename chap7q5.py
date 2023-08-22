#program to sum n numbers before given natural number
n=int(input("please enter number"))
sum=0
while n>0:
    sum=sum+n
    n=n-1
print(sum)