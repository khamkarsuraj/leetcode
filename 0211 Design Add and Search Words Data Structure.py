# Trie with dfs
# time
    # add n
    # search without . n
    # search with . 26^n
# space n

class Node:
    def __init__(self):
        self.childerns = {}
        self.is_last = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        n = self.root
        for char in word:
            if char not in n.childerns:
                n.childerns[char] = Node()
            n = n.childerns[char]
        n.is_last = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: Node):
            if index == len(word):
                return node.is_last

            char = word[index]
            if char == '.':
                for child in node.childerns.values():
                    if dfs(index+1, child):
                        return True
                return False
            elif char in node.childerns:
                return dfs(index+1, node.childerns[char])
            else:
                return False
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
