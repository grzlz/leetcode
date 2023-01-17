# Given an array of integers, write a function that moves all 0's to the end while maintaining the relative order of the other elemnts

array = [1, 0, 3, 5, 3, 2, 0, 3, 0, 1]

# Use two pointer strategy

def move_zeros(array):
    j = 0
    for number in array:
        if number != 0:
            array[j] = number
            j += 1

    while j < len(array):
        array[j] = 0
        j+=1

    print(array) 

move_zeros(array)