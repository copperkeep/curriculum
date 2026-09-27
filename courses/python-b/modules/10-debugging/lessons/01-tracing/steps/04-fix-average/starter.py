def average(nums):
    total = 0
    for i in range(1, len(nums)):
        total = total + nums[i]
    return total / len(nums)
