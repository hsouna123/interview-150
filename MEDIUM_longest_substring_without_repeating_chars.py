class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cim = {}
        start = 0 
        max_len = 0
        for end in range(len(s)):
            if s[end] in cim and cim[s[end]] >= start:
                start = cim[s[end]] + 1
            cim[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len 
