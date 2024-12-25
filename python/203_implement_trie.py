class Trie:

    def __init__(self):
        self.children = {} # dict of Trie's
        self.isWord = False

    def insert(self, word: str) -> None:
        if not word:
            self.isWord = True
            return
        first_char = word[0]
        if first_char not in self.children:
            self.children[first_char] = Trie()
        self.children[first_char].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.isWord

        first_char = word[0]
        if first_char not in self.children:
            return False

        return self.children[first_char].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True

        first_char = prefix[0]
        if first_char not in self.children:
            return False

        return self.children[first_char].startsWith(prefix[1:])

# ["Trie","insert","search","search","startsWith","insert","search"]
# [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
