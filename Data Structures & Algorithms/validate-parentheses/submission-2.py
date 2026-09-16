class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        openBrackets = ["{", "[", "("]
        hashmap = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
        
        for char in s:
            if char in openBrackets:
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                temp = stack.pop()
                if char != hashmap[temp]:
                    return False

        if len(stack) != 0:
            return False

        return True

