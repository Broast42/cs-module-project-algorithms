'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    # Your code here
    # First pass solution
    #create new array to return
    new_arr = []
    #create a k-index var to track index needed to keep window within k: set to k
    k_index = k
    #loop through the original array up to lenghth - (k -1)
    for i in range(len(arr) - (k - 1)): 
        #for each index splice array starting at index and ending at k-index var 
        splice = arr[i:k_index]
        #take splice and find max value and append it to new array
        max_value = max(splice)
        new_arr.append(max_value)
        #increment k_index by 1
        k_index += 1
    #return new array
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
