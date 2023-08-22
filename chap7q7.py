for i in range(1,6):
    for space in range(1,6-i):
        print(" ",end="")
    for stars in range(1,(i*2-1)+1):
        print("*",end="")
    print("\n")