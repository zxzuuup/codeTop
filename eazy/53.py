def maxSubArray(self, nums):
    maxVal = nums[0]
    res = nums[0]
    for num in nums[1:]:
        maxVal = max(maxVal+num, num)
        res =max(res, maxVal)
    return res