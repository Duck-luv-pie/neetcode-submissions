class PrefixTree:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def insert(self, word: str) -> None:
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = PrefixTree()
            root = root.children[c]
        root.end_of_word = True


    def search(self, word: str) -> bool:
        root = self
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        root = self
        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True
        