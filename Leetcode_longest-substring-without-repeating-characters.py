#https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Below is my solution but failed to go through all test cases
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = s
        temp = []
        for i in range(len(s)):
            if s[i] not in temp:
                temp.append(s[i]) 
                
        listtostr = ''.join(map(str,temp))
        return(len(listtostr))
        
        
# better solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[c] = i
            
        return(max_length)