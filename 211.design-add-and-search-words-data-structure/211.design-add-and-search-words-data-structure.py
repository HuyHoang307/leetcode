from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.word_dictionary = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.word_dictionary[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.word_dictionary[len(word)]

        for w in self.word_dictionary[len(word)]:
            for i, char in enumerate(word):
                if  char != w[i] and char != '.':
                    break
            else:
                return True
        return False

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True
    
