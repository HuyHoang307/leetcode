class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = [homepage]
        self.forward_stack = []
        

    def visit(self, url: str) -> None:
        self.back_stack.append(url)
        self.forward_stack.clear()
        

    def back(self, steps: int) -> str:
        while steps and len(self.back_stack) > 1:
            url = self.back_stack.pop()
            self.forward_stack.append(url)
            steps -= 1
        return self.back_stack[-1]
        

    def forward(self, steps: int) -> str:
        while steps and len(self.forward_stack) > 0:
            url = self.forward_stack.pop()
            self.back_stack.append(url)
            steps -= 1
        return self.back_stack[-1]
    
b = BrowserHistory("leetcode.com")
print(b.visit("google.com"))
print(b.visit("facebook.com"))
print(b.visit("youtube.com"))
print(b.back(1))
print(b.back(1))
print(b.forward(1))
print(b.visit("linkedin.com"))
print(b.forward(2))
print(b.back(2))
print(b.back(7))
