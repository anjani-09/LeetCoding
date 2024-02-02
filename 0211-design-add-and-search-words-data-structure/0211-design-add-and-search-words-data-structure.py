class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.End = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNode()
            current = current.children[w]
        current.End = True

    def search(self, word: str) -> bool:
        current = self.root
        def dfs(j, current):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in current.children:
                        return False
                    current = current.children[word[i]]
            return current.End
        return dfs(0, current)
            
        
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)