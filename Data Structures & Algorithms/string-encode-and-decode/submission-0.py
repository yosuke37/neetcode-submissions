class Solution:
    def encode(self, strs: List[str]) -> str:
        # Prefix each string with its length and a delimiter, e.g. "5#Hello"
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the delimiter '#' to read the length prefix
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length
        return result