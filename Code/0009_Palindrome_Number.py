class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if  str(x) == str(x)[::-1] and x < 2**31-1:
            return True
        else:
            return False
