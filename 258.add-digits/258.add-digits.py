class Solution:
  def addDigits(self, num: int) -> int:
    if num < 10:
      return num
    res = num % 9
    return res if res else 9
    
num = 20
s = Solution()
print(s.addDigits(num))