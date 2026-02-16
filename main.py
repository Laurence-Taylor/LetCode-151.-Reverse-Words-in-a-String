class Solution:
    def reverseWords(self, s: str) -> str:
        # split the string
        s = s.split()
        # reverse the string
        s = reversed(s)
        # join the string and return it
        return " ".join(s)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("Your reversed string should not contain leading or trailing spaces"))