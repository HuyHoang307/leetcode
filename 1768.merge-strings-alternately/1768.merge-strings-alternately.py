class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        st = ""
        for i in range(n):
            st += word1[i] + word2[i]
        return st+word1[n:]+word2[n:]

word1 = "ab"
word2 = "pqrs"
s = Solution()
print(s.mergeAlternately(word1, word2))
