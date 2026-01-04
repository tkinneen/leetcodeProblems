# LeetCode Problem 211: Design Add and Search Words Data Structure
#
# Design a data structure that supports adding new words and finding if a string 
#    matches any previously added string.
#
# Implement the WordDictionary class:
# 
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that 
#    matches word or false otherwise. word may contain dots '.' where dots can be 
#    matched with any letter.

#
class TrieNode:
	def __init__(self):
		self.children = {}
		self.endOfWord = False
		
class WordDictionary:

    # addWord, Time: O(L) where L is the length of the word
    # addWord, Space: O(L) worst case per added word, or O(N) where N is the total
    #    number of chars across all inserted words
    # search, Time: O(L) if there are no wildcards, or O(a^d * L) where a is the
    #    number of letters in the alphabet and d is the number of dot chars in the 
    #    search word
    # search, space: O(L) on account of the recursion stack

    def __init__(self):
        self.root = TrieNode()
    
    # Go char by char through a word, checking each step if a TrieNode exists for
    #    it and creating one if it doens't
    def addWord(self, word: str) -> None:
        
        # Set a pointer to the root of the trie structure
        current = self.root
        
        # Loop through each character of the word being added
        for char in word:
            
            # Check whether this character is adjacent to the current character,
            #    and create a brand new Trie node for it if it does not yet exist
            if char not in current.children:
                current.children[char] = TrieNode()
            
            # Regardless of whether the node already existed or was just created, 
            #    traverse to the next letter's TrieNode
            current = current.children[char]
        
        # Once all characters have been added, set flag denoting a complete word
        current.endOfWord = True
    

    # Because this solution specifies 'dot' wildcard characters that 
    def search(self, word: str) -> bool:
        
        # Create a helper function that allows us to recurse to find all matches for
        #    "wildcard" letters. Providing a start index and its corresponding node
        #    allows us to "start fresh" anytime we need to branch into multiple paths
        def dfs(startIdx, curNode):
            
            # Create a pointer to the current TrieNode
            cur = curNode

            # Loop from the start index to the end of hte word
            for i in range(startIdx, len(word)):
                
                # Use our start index to grab the character we're currently searching
                char = word[i]

                # Current character is a "dot" wildcard, we must recursively branch and 
                #    continue the search for all this character's child nodes
                if char == ".":

                    # We will branch off here into however many instances as this trie 
                    #    node has children, each going to the end of the line
                    for child in cur.children.values():

                        # Recurse into our helper function, passing in the next character's index and corresponding TrieNode
                        # We will either find a valid word and bubble up True, or exhaust the dot's child paths and return False
                        if dfs(i + 1, child):
                            return True
                    
                    # This will only return false if NONE of the children come back
                    #    with a valid word, so it doesn't matter if you have to branch 
                    #    with another dot character further down in recursion, as one 
                    #    of those will have to return true before we make it back here
                    return False
                
                else: # regular case, NOT a wildcard

                    # If the current char does not appear in children, then the word doesn't exist and we return false
                    if char not in cur.children:
                        return False

                    # Otherwise shift to the current letter's trie node and continue looping
                    cur = cur.children[char]
            
            # We've made it to the last letter of the word we're searching for, so as
            #   long as the endOfWord flag has been set correctly it will return True 
            return cur.endOfWord
        
        # Kick off recursion by passing in the zeroth index of the search word and the root node of the Trie
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)	