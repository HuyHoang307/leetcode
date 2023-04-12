class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        res = []
        for word in path.split('/'):
            if word == '..':
                if len(res) > 0:
                    res.pop()
            elif word and word != '.':
                res.append(word)

        return '/' + '/'.join(res)
    

path = "/home//foo/"
s = Solution()
print(s.simplifyPath(path))
