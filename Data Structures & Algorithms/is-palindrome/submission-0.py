class Solution:
    def isPalindrome(self, s: str) -> bool:

        f, l = 0 , len(s) - 1

        while f<l:
            while f < l and not self.alphaNum(s[f]):
                f  = f + 1
            while l > f and not self.alphaNum(s[l]):
                l = l -1
            if s[f].lower() != s[l].lower():
                return False
            f  = f + 1
            l = l -1

        return True

    def alphaNum(self, c):
            return (
                ord('A') <= ord(c) <= ord('Z')or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
            )



            
        