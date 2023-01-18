# Find if there is an increasing subarray followed by a decreasing subarray 

def valid_mountain(array):
    if len(array) < 3:
        print("Please introduce a valid array.")

    else:
        incresing_pointer_end = 0
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                pass
                
            elif array[i] > array[i + 1]:   
                incresing_pointer_end = i

        for i in range(incresing_pointer_end, len(array) - 1):
            if array[incresing_pointer_end] > array[i + 1]:
                return True
            
            else:
                return False

        if incresing_pointer_end == 0:
            return False

arr = [0 , 1, 0]

print(valid_mountain(arr))