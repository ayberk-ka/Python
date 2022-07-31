list=[1, 30,100,50,3,60,2,59,44,20]
def binarySearch(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
            
        elif arr[mid] > x:
                return binarySearch(arr, low, mid -1, x)

        else:
                return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

arr= sorted(list)
x = int(input('Enter the value: '))


result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")