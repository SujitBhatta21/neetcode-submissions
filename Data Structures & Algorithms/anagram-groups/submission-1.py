class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            char_map = [0]*26
            for j in i:
                char_map[ord(j) - ord('a')] += 1
            char_map = tuple(char_map)
            if char_map in res:
                res[char_map].append(i)
            else:
                res[char_map] = [i]        
        return list(res.values())
     