class Node:
    def __init__(self, is_word: bool):
        self.children = {}
        self.is_word = is_word