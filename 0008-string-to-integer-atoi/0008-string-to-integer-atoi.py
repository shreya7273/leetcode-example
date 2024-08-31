class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
    
        i = 0
        sign = 1
        n = len(s)
        
        
        while i < n and s[i] == ' ':
            i += 1
        
        
        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
    
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num