class TrieNode:
    def __init__(self, children=None, is_end=False):
        self.children = children if children is not None else {}
        self.is_end = is_end
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        index = 0

        while index < len(word):
            character = word[index]

            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]
            index += 1

        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        index = 0

        while index < len(word):
            character = word[index]

            if character not in current.children:
                return False

            current = current.children[character]
            index += 1

        return current.is_end == True

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        index = 0

        while index < len(prefix):
            character = prefix[index]

            if character not in current.children:
                return False

            current = current.children[character]
            index += 1

        return True        
        