class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_substring = ""
        max_string = ""
        for i in s:
            if (i in long_substring) == False: # char not in string
                long_substring += i
                
            elif (i in long_substring) == True: # char in string
                if len(max_string) < len(long_substring):
                    max_string = long_substring
                
                # find repeat char, and start from second word
                repeat_index = long_substring.index(i)
                long_substring = long_substring[repeat_index + 1:] + i

            # override substring
            if len(max_string) < len(long_substring):
                max_string = long_substring
        return len(max_string)
