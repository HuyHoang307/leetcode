from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        head = 0
        stack = []
        for num in pushed:
            if num == popped[head]:
                head += 1
                while len(stack) and stack[-1] == popped[head]:
                    stack.pop()
                    head += 1
            else:
                stack.append(num)
        return len(stack) == 0

              

pushed = [1, 2, 3, 4, 5]
popped = [3, 2, 5, 4, 1]
s = Solution()
print(s.validateStackSequences(pushed, popped))