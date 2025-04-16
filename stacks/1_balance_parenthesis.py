"""
Balance Parenthesis

Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

""" 


class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        match_brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for ch in s:
            if ch in match_brackets.values():
                stack.append(ch)
                
            elif ch in match_brackets:
                if len(stack) > 0 and stack[-1] == match_brackets[ch]:
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0
    
        
res = Solution()

print(res.isBalanced("[{()}]")) # True
print(res.isBalanced("[()()]{}")) # True
print(res.isBalanced("([{]})")) # False


