class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                if stack and stack[-1] == bracket_map[char]:
                    # if closed by the same type of brackets then pop out
                    stack.pop()
                else:
                    return False
            else:
                # add new bracket, cause need to confrim whether it has closed by the same type of brackets
                stack.append(char)
        
        # it should be null in stack, or return False
        return not stack
