class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = ["(", "{", "["]
        closing_brackets = [")", "}", "]"]
        bracket_mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if len(stack) == 0 or stack.pop() != bracket_mapping[char]:
                    return False
        
        return not len(stack)