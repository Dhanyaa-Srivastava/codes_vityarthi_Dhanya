def partition_function(n):
    """
    Compute the partition function p(n) which counts the number of ways 
    to represent n as a sum of positive integers, order disregarded.
    
    Uses a dynamic programming approach based on Euler's pentagonal number theorem.
    """
    # Initialize a list p where p[k] will store p(k)
    p = [0] * (n + 1)
    p[0] = 1  # Base case: only one way to partition 0
    
    for k in range(1, n + 1):
        total = 0
        j = 1
        while True:
            # Generalized pentagonal numbers: j(3j-1)/2 and j(3j+1)/2
            pent1 = j * (3 * j - 1) // 2
            pent2 = j * (3 * j + 1) // 2
            if pent1 > k and pent2 > k:
                break
            
            sign = -1 if (j % 2 == 0) else 1
            
            if pent1 <= k:
                total += sign * p[k - pent1]
            if pent2 <= k:
                total += sign * p[k - pent2]
                
            j += 1
        
        p[k] = total
    
    return p[n]

# Example usage:
n = 5
print(f"The number of partitions of {n} is {partition_function(n)}")  # Output: 7
