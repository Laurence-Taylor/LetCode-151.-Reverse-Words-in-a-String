class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string
        words = s.split()
        # reverse the string
        reversed_words = reversed(words)
        # join the string and return it
        return " ".join(reversed_words)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("Your reversed string should not contain leading or trailing spaces"))