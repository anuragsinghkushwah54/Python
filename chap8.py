#we are using function to print anurag. it is first program which uses function
def fun1():
    print("hello anurag",end=". ") 
fun1()
# practice set chapter 8 question number 1st. make function to find highest from given three value
def max(a,b,c ):
    if(a>b):
        if(a>c):
            print("max value is : ",a)
    elif(b>c):
        print("max value is :",b)
    else:
        print("max value is :",c)

a=int(input("please enter first value :"))
b=int(input("please enter second value :"))
c=int(input("please enter last value :"))
max(a,b,c)

# practice set chapter 8 question number 2nd. convert celsius to feranite
def convert(celsius):
    k=(celsius*9/5)+32
    print("given celsius in feranite is :",k)
celsius=int(input("please enter celsius for conversion"))
convert(celsius)

# practice set chapter 8 question number 3rd. prevent print function to give next line after statement
# we prevent print function using end argument ex-line number 3

#practice set chapter 8 question number 4th.write a recursive function to calculate sum of first n natural numbers

def natural_num(nn):
    natural=0
    while(nn>0):
        natural=natural+nn
        nn=nn-1
    return natural
nn=int(input("please enter number for natural submittion :"))
natural1=natural_num(nn)
print("submittion of firt natural is :",natural1)

#pracctice set chapter 8 question number 4th, write function to print following pattern
star1=int(input("how many times. you want to print star"))
def star(star1):
    for j in range(0,star1):
        for i in range(0,star1-j):
            print("*",end="")
        print("\n",end="")
star(star1)
