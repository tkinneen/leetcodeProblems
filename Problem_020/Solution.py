# LeetCode Problem 020: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', 
#    '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        
        # This dictionary is going to hold ONLY opening brackets, in the order they appear
        #    in the string. We use this to ensure open brackets are closed in the correct 
        #    order. When a bracket gets closed correctly, we pop it's opener out of the stack.
        bracketStack = []

        # The keys of this hashmap are all closers, we use it to check its corresponding opener 
        mapBrackets = { ')' : '(', ']' : '[', '}':'{' }

        for currBracket in s:
            
            # If this is a closing char - keys in hash map are each type of closing paren
            if currBracket in mapBrackets:
                # Stack can't be empty, and the last item in the stack 
                if bracketStack and bracketStack[-1] == mapBrackets[currBracket]:
                    bracketStack.pop()
                else:
                    return False
            else:
                # Because it's not in the hashmap, we know the current bracket is an opener. Put 
                #    it in the stack.
                bracketStack.append(currBracket)
        
        # If we reached the end of the bracket string and the stack is empty, all pairs were closed 
        #    successfully. If not the bracket string is invalid.
        if not bracketStack:
            return True
        else:
            return False
            
