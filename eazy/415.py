class Solution:
    def addStrings(self, num1: str, num2: str):
        res = ''
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num1[j]) - ord('0') if j >= 0 else 0

            val = a + b + carry
            res += str(val % 10)
            carry = val // 10
            i, j = i - 1, j - 1
        if carry > 0:
            res += str(carry)

        return res[::-1]
