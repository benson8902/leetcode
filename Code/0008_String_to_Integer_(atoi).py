import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # remove space
        s = s.strip()
        if not s:
            return 0
        
        # select the first part of words
        s = s.split()[0]

        # check Signedness
        if len(s) > 1 and (s[0] in ('-', '+') and s[1] in ('-', '+')) or s.find('.') == 0:
            return 0
        elif s.find('-') == 0:
            negative = True
        else:
            negative = False

        
        if re.match(r'[+-]?\d+', s):
            num = re.search(r'\d+', s)
        else:
            return 0
        
        if num:
            num = num.group()
        else:
            return 0

        # give signedness
        if negative:
            num = int(num)*(-1)
        else:
            num = int(num)
            
        # if out of range then give maximun or minimum
        if num > 2 ** 31 - 1:
            num = 2 ** 31 -1
        elif num < -2 ** 31:
            num = -2 ** 31
            
        return num
