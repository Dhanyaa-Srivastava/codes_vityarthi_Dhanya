def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    lucas_nums = [2, 1]
    for i in range(2, n):
        next_num = lucas_nums[i - 1] + lucas_nums[i - 2]
        lucas_nums.append(next_num)
    return lucas_nums

n = int(input("Enter the number of Lucas numbers to generate: "))
print(lucas_sequence(n))
