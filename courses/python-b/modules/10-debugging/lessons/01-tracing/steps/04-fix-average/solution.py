def average(nums):
    total = 0
    for i in range(0, len(nums)):
        total = total + nums[i]
    return total / len(nums)
