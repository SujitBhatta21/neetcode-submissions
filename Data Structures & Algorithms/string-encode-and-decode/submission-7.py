class Solution:
    def encode(self, strs: List[str]) -> str:
        self.TOKEN = "v1AFSz6wiCPPX0rYitb1Orp+j1FHVhSyBKQw61CXnJE="
        
        encoded_string = ""

        for i in strs:
            encoded_string += i + self.TOKEN
        return encoded_string

    def decode(self, s: str) -> List[str]:
        s = s.split(self.TOKEN)
        s.pop()
        return s