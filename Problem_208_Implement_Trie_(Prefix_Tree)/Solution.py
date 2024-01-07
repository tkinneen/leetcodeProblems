# LeetCode Problem 208: Implement Trie (Prefix Tree)
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used
#    to efficiently store and retrieve keys in a dataset of strings. There
#    are various applications of this data structure, such as autocomplete
#    and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
#
# void insert(String word) Inserts the string word into the trie.
#
# boolean search(String word) Returns true if the string word is in the trie
#    (i.e., was inserted before), and false otherwise.
#
# boolean startsWith(String prefix) Returns true if there is a previously
#    inserted string word that has the prefix prefix, and false otherwise.

# Definition for a binary tree node.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        # Start at the root node
        currentTrieNode = self.root

        # Loop through each letter of the word being inserted
        for currentLetter in word:
            
            # Check if a TrieNode for that letter already exists
            if currentLetter not in currentTrieNode.children:
                
                # If it does not, we will create a node for the current letter
                currentTrieNode.children[currentLetter] = TrieNode()

            # Shift nodes to the next letter
            currentTrieNode = currentTrieNode.children[currentLetter]

        # Once the entire word has been processed, set the endOfWord flag to True
        currentTrieNode.endOfWord = True

    def search(self, word: str) -> bool:
        
        # Start at the root node
        currentTrieNode = self.root

        # Loop through each letter of the word we're searching for
        for currentLetter in word:

            # If there is no node for the current letter, return False
            if currentLetter not in currentTrieNode.children:
                return False
            
            # If there is a node for the current letter, traverse to it
            currentTrieNode = currentTrieNode.children[currentLetter]

        # When all letters are exhausted, return the endOfWord flag. If it is 
        #    a word that has been inserted previously, it will be True
        return currentTrieNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        # Start at the root node
        currentTrieNode = self.root

        # Loop through each letter of the prefix we're searching for
        for currentLetter in prefix:

            # If there is no node for the current letter, return False
            if currentLetter not in currentTrieNode.children:
                return False
            
            # If there is a node for the current letter, traverse to it
            currentTrieNode = currentTrieNode.children[currentLetter]
        
        # Every letter of the prefix contains a vaild node, so a word has been
        #    inserted that starts with the prefix
        return True