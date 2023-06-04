def twoSum(self, nums, target):
    hashDict = dict()
    for index, val in enumerate(nums):
        if target - val in hashDict:
            return [hashDict[target - val], index]
        else:
            hashDict[val] = index
    return None