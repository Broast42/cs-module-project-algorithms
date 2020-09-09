'''
Input: an integer
Returns: an integer
'''

from itertools import product 

def eating_cookies(n, cache):
    # Your code here
    #first pass solution
    #track diference in n between recurtions using cache index 0
    diff = cache[0]
    #set base case when cookies equal 0 
    if n == 0:
        #return sum of cache
        total = sum(cache) - cache[0]
        if total == 0:
            return 1
        return total    
    else:
        #find all combos at n+diff places using itertools product
        combos = list(product([1, 2, 3], repeat=n))
        #loop through combos and if the sum adds up to n increment cache += 1 at index n
        for i in combos:
            if sum(list(i)) == n+diff:
                cache[n] += 1
        #add 1 to diff
        cache[0] += 1
        #recursivly call eating cookies with value n-1
        return eating_cookies(n-1, cache)
    #return cache
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 0

    print(f"There are {eating_cookies(num_cookies,[0 for i in range(num_cookies+1)] )} ways for Cookie Monster to each {num_cookies} cookies")
    