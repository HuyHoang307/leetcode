from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        check = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif not stack or stack.pop() != check[i]:
                return False

        if not stack:
            return True
        else:
            return False
        

s = '()[]{}'
solution = Solution()
print(solution.isValid(s))