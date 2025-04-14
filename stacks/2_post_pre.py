''' 
You are given a string that represents the postfix form of a valid mathematical expression. 
Convert it to its prefix form.
''' 

#  ABC/-AK/L-*        : postfix
#  A-(B/C) * (A/K)-L  : infix
#. *-A/BC-/AKL        : prefix

class Solution:
    def postToPre(self, post_exp):
        # Code here
        stack = []
        operators = "+-*/^%"
        
        for ch in post_exp:
            if ch not in operators:
                stack.append(ch)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                infix = stack.append(ch + op2 + op1)
        
        return stack.pop()
                
ans = Solution()

print(ans.postToPre("ABC/-AK/L-*"))
print(ans.postToPre("ab+"))


