class Node:
    def __init__(self):
        self.childern = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.childern:
                node.childern[char] = Node()
            node = node.childern[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.childern:
                return False
            node = node.childern[char]
        return node.is_end
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.childern:
                return False
            node = node.childern[char]
        return True   
