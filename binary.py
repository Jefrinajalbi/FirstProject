def BinarySearch(arr,target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = round(start+(end-start)/2)
        if(target>arr[mid]):
            start=mid+1
        elif(target<arr[mid]):
            end=mid-1
        else:
            return mid
    return -1
arr=[-10,-7,-2,-1,0,2,4,6,9,14,19,30,45,59,60,70,80]
target = -2
result = BinarySearch(arr,target)
print(result)
