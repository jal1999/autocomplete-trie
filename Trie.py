"""
An implementation of the trie data structure.

This will be used to solve the problem of creating an auto-complete
functionality that returns the list of all words in a given collection
that have a given prefix.

Author: James LaFarr
Version: 12.2.22
"""

from Node import Node

class Trie:
    def __init__(self, words: list[str]):
        """
        Initializes the trie with a root node, and
        builds the trie with the given collection of words.

        :param words: collection of words to build the trie with
        :type words: list[str]
        """
        self.root = Node(False)
        self.build(words)


    def build(self, words: list[str]):
        """
        Builds the trie with a given list of words.

        :param words: list of words to put in the trie
        :type words: list[str]
        :returns: None
        """
        for word in words:
            curr_node: Node = self.root
            for char in word:
                if not char in curr_node.children:
                    curr_node.children[char] = Node(False)
                curr_node = curr_node.children[char]
            curr_node.is_word = True


    def find_words_from_node(self, node: Node, curr_word, words=[]) -> list[str]:
        """
        Finds all words that can be reached from the current node.

        For each child of the current node, the function will check if
        the child forms a complete word, and if so will add it to the
        collection of words, and if the child doesn't form a complete
        word, it ignores it.

        After the complete word is added to the collection or the node
        is ignored, the function will recurse on the child.

        :param node: the current node in the trie
        :type node: Node
        :param curr_word: the current word, created by the accumulation of all past nodes
        :type curr_word: str
        :param words: collection keeping track of words reachable from curr_node
        :type words: list[str]
        :return: collection of words that are reachable from the given node
        :type: list[str]
        """
        for (key, child) in node.children.items():
            if child.is_word:
                words.append(curr_word + key)
            self.find_words_from_node(child, curr_word + key, words)
        return words


    def autocomplete(self, prefix: str) -> list[str]:
        """
        Navigates to the node that contains the last character of
        the given prefix, and calls find_words_from_node() in order to
        compute the words reachable from the prefix node.

        :param prefix: the prefix of all words returned
        :type prefix: str
        :return: collection of words in the trie with the given prefix
        :rtype: list[str]
        """
        curr_node: Node = self.root

        for char in prefix:
            if char not in curr_node.children: # prefix doesn't exist in tree
                return []
            curr_node = curr_node.children[char]
        return self.find_words_from_node(curr_node, prefix)

