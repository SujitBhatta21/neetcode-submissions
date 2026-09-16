class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashtable = {}
        t_hashtable = {}

        if len(t) != len(s):
            return False

        for i in s:
            if i in hashtable:
                hashtable[i] += 1

            else:
                hashtable[i] = 1

        for j in t:
            if j in t_hashtable:
                t_hashtable[j] += 1
            else:
                t_hashtable[j] = 1

        for k in s:
            if k not in t_hashtable:
                return False

            if hashtable[k] != t_hashtable[k]:
                return False

        return True