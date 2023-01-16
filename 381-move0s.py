# Given an array of integers, write a function that moves all 0's to the end while maintaining the relative order of the other elemnts

array = [1, 2, 3, 0, 4, 5, 0, 3]

def move_zeros(array):
    zeros_positions = []
    for i in range(len(array)):
        if array[i] == 0:
            zeros_positions.append(i)

 

    for i in zeros_positions:
        del array[i]

    for i in range(len(zeros_positions)):
        array.insert(i, 0)

    print(array)

move_zeros(array)