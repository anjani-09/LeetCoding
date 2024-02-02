class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.End = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.End = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.End
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            if w not in current.children:
                return False
            current = current.children[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)