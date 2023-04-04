class Solution:
    def partitionString(self, s: str) -> int:
        st = []
        running = "" 
        for c in s: 
            if c in running: 
                st += [running] 
                running = ""
            running += c
        return len(st) + 1
    
s = "ssssss"
solution = Solution()
print(solution.partitionString(s))