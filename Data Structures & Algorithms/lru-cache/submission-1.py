class Node():
    def __init__(self, left, right, key, val):
        self.left = left
        self.right = right
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.start = None
        self.end = None
        self.capacity = capacity
        self.mapping = {}

    def update_position(self, key: int) -> None:
        node = self.mapping[key]

        if node == self.end:
            return

        if node == self.start:
            self.start = node.right
            self.start.left = None
        else:
            node.left.right = node.right
            node.right.left = node.left

        node.left = self.end
        node.right = None
        self.end.right = node
        self.end = node

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.update_position(key)
            return self.mapping[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.end == None:
            self.start = self.end = Node(None, None, key, value)
            self.mapping[key] = self.end
        elif key in self.mapping:
            self.mapping[key].val = value
            self.update_position(key)
            return
        else:
            self.end.right = Node(self.end, None, key, value)
            self.end = self.end.right
            self.mapping[key] = self.end
            if len(self.mapping) > self.capacity:
                old_start = self.start
                self.start = self.start.right
                self.start.left = None
                del self.mapping[old_start.key]
            return 
                
            
        
