class Node:
    def __init__(self, value=None, is_terminal=False):
        self.children = {}
        self.value = value
        self.is_terminal = is_terminal

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(value=char)
            node = node.children[char]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.search("app")
param_4 = obj.startsWith("app")
print(param_2, param_3, param_4)
