from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n==0:
            return 0
        walker = 1
        count = 1
        check = chars[0]
        for i in range(1, n):
            if chars[i] == check:
                count += 1
            else:
                if count > 1:
                    for digit in str(count):
                        chars[walker] = digit
                        walker += 1
                check = chars[i]
                chars[walker] = check
                walker += 1
                count = 1
        if count > 1:
            for digit in str(count):
                chars[walker] = digit
                walker += 1
        return chars
                
chars = ["a","a","a","b","b","a","a"]
s = Solution()
print(s.compress(chars))