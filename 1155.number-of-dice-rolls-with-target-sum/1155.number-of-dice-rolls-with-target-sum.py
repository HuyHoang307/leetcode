class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.res = 0
        memo = {}
        def helper(d,target):
            if target <= 0 or target > (d * f):
                return 0
            if d == 1:
                return 1 
            if (d, target) in memo:
                return memo[(d, target)]
            ret = 0 
            for i in range(1,f+1):
                ret += helper(d-1,target-i)
            memo[(d,target)] = ret
            return memo[(d,target)]
        

        return helper(d,target) % (10**9 + 7)