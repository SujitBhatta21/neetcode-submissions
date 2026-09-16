class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 1
            else:
                a[s[i]] += 1
            if t[i] not in b:
                b[t[i]] = 1
            else:
                b[t[i]] += 1

        for key in a:
            if key not in b:
                return False
            else:
                if a[key] != b[key]:
                    return False
        return True