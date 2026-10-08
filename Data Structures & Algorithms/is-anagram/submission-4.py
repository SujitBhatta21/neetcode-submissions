class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        for i in t:
            if i in count:
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
            else:
                return False
        if len(count) == 0:
            return True
        return False