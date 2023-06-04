class Solution:
    # 快速选择
    def findKthLargest(self, nums, k):
        length = len(nums)
        target = length - k
        left = 0
        right = length - 1
        while left <= right:
            pivot = self.partition(nums, left, right)
            if pivot == target:
                return nums[pivot]
            if pivot < target:
                left = pivot + 1
            if pivot > target:
                right = pivot - 1

    def partition(self, nums, left, right):
        nums[left], nums[(left + right) >> 1] = nums[(left + right) >> 1], nums[left]
        val = nums[left]
        index = left + 1
        for i in range(left + 1, right + 1):
            if nums[i] <= val:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        index -= 1
        nums[left], nums[index] = nums[index], nums[left]
        return index


    # 堆排
    def findKthLargest2(self, nums, k):
        
