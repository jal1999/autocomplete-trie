"""
Data store to represent a node in a trie.

Author: James LaFarr
Version: 12.2.22
"""

class Node:
    def __init__(self, is_word: bool):
        self.children = {}
        self.is_word = is_word