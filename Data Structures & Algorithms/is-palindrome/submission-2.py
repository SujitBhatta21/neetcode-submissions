class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        N = len(s)
        l = 0
        r = N - 1
        
        while l <= r:
            while l < r and not self.checkChar(s[l]):
                print(s[l])
                l += 1
            while l < r and not self.checkChar(s[r]):
                r -= 1
            if s[r] != s[l]:
                return False
            l += 1
            r -= 1
        return True

    def checkChar(self, char):
        return (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('0') and ord(char) <= ord('9'))