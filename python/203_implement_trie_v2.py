class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]

        current["*"] = ""

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]

        return "*" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]

        return True

    def __repr__(self):
        return str(self.root)


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))