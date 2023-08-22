import time
print("hello sir. please enter your name")
a=input()
tm=int(time.strftime("%H"))
if tm>0 and tm<12:
    print("good morning",a)