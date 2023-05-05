class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        for i in s[0:k]:
            if i in vowels:
                count += 1
        if count == k:
            return count
        largest = count
        for i in range(len(s)-k):
            if s[i] in vowels:
                count -= 1
            if s[i+k] in vowels:
                count += 1
            if count == k:
                return count
            elif count > largest:
                largest = count
        return largest


s = "aeiou"
k = 2
sol = Solution()
print(sol.maxVowels(s, k))
