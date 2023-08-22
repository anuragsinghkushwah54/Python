def bubble(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-1-i):
         if arr[j] < arr[j+1]:
            arr[j],arr[j+1]==arr[j+1],arr[j]
            swapped=True
        if (swapped==False):
                break
__name__="__main__"
arr=[1,5,3,56]
bubble(arr)
for i in range(len(arr)):
    print(arr[i])
