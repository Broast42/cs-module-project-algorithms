
'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    #first pass solution
    #create a new empty array to add the product values to
    new_arr = []
    #loop through array
    for i in range(len(arr)):
        #create a copy of arr to manipulate
        copy = []
        copy += arr
        #delete entry at current index from copied array
        del copy[i]
        #get product of copied array and append it to new array
        product = 1
        for i in copy:
            product *= i

        new_arr.append(product)
    #return new array
    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
