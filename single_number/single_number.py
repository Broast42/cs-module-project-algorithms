'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    #first pass solution
    single_num = 0
    #get the largest number in the array and add 1
    max_num = max(arr) + 1
    #create a count array of zeros the size of max number in arr
    count_arr = [0] * max_num 
    #for every item in arr check its value and increment count array +1 at index of that value
    for i in arr:
        count_arr[i] += 1
    #loop through count array if value is equal to 1 return that index
    for i in range(len(count_arr)):
        if count_arr[i] == 1:
            single_num = i

    return single_num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
