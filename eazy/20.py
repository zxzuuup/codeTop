
# 自己的解法
def isValid(s: str):
    hash = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    stack = []
    for v in s:
        if v == '[' or v == '(' or v == '{':
            stack.append(v)
        elif len(stack) > 0 and hash[v] == stack[len(stack) -1]:
            stack = stack[:len(stack) - 1]
        else:
            return False
    return len(stack) == 0


# 网上解法

def isValid2(s: str):
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in s:
        if stack and i in dic:
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack
