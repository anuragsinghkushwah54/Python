num=int(input("input number"))
condition=False
if num==1:
    print("it is not prime number")
else:
    for i in range(2,num):
        if(num%i)==0:
            condition=True
            break
if condition:
    print("condition is not prime number")
else:
    print("number is prime number")