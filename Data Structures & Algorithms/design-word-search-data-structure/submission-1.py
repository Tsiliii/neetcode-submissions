class TrieNode:
    def __init__(self, children=None, is_end=False):
        self.children = children if children is not None else {}
        self.is_end = is_end

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        current = self.root
        index = 0

        while(index < len(word)):
            character = word[index]

            if character not in current.children:
                current.children[character] = TrieNode()
            
            current = current.children[character]
            index += 1

        current.is_end = True
        
    def search(self, word: str) -> bool:

        def backtrack(current, index):
            if index == len(word):
                return current.is_end

            character = word[index]

            if character == ".":
                for child in current.children.values():
                    if backtrack(child, index + 1):
                        return True

                return False

            if character not in current.children:
                return False

            return backtrack(current.children[character], index + 1)

        return backtrack(self.root, 0)