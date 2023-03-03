class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        n1 = len(haystack)
        n2 = len(needle)
        def compare(s1: str, s2: str, start: int):
            for c in s2:
                if c != s1[start]:
                    return False
                else:
                    start += 1
            return True
        
        for i in range(n1 + 1 - n2):
            if haystack[i] == needle[0]:
                if compare(haystack, needle, i):
                    return i
        return -1
