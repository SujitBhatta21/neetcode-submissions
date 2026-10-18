class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for i in s:
            if not i in brackets:
                stack.append(i)
            else:
                if stack and stack[-1] == brackets[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
