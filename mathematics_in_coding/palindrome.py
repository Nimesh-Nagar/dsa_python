class Solution:
    # nave approch
    def isPalindrome(self, x: int) -> bool:
        rev = 0 
        temp = x

        if temp >= 0:
            while temp != 0:
                unit = temp % 10 
                rev = rev * 10 + unit
                temp = temp // 10 

            if x == rev:
                return True
            else:
                return False
        else: 
            return False  

    # efficient approch 
    def efficient_sol(self, x: int) -> bool:
        x_str = str(x)
        if x_str[::-1] == x_str:
            return True
        else:
            return False


s1 = Solution()
print(s1.isPalindrome(-121)) 
print(s1.efficient_sol(16521))      
