list=[1, 30,100,50,3,60,2,59,44,20]
def binarySearch(arr, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
                
        elif arr[mid] < x:
             low = mid + 1

        else:
            high = mid - 1
    return 'Not Found'        

arr = sorted(list)
x = int(input('Enter the value: '))


result = binarySearch(arr, x, 0, len(arr)-1)

if result != 'Not Found':
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
