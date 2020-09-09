'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #first pass solution
    #create a new empty array
    new_arr = []
    #loop through the arr 
    for i in arr:
        #if element is zero append new arr with element
        if i == 0:
            new_arr.append(i)
        else:
            new_arr.insert(0, i)
        #else insert element at index 0 in new arr
    #return new array
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")