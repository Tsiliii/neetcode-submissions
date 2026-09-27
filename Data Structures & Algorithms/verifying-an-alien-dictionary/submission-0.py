class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, char in enumerate(order):
            order_dict[char] = i

        def ordered(order_dict, left, right):
            for i in range(min(len(left), len(right))):
                if order_dict[left[i]] > order_dict[right[i]]:
                    return False
                elif order_dict[left[i]] < order_dict[right[i]]:
                    return True

            return len(left) <= len(right)
            
        current_word = words[0]
        for i in range(len(words)):
            if not ordered(order_dict, current_word, words[i]):
                return False
            current_word = words[i]
        return True
            