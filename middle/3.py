class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = dict()
        leftVal = 0
        maxLen = 0
        for index in range(0,len(s)):
            val = s[index]
            if val in map.keys():
                leftVal = max(leftVal, map[val] + 1)
            map[val] = index
            maxLen = max(maxLen, index - leftVal + 1)
        return maxLen