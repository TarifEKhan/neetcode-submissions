class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char.lower() for char in s if char.isalnum())
        print (clean_text)
        return clean_text == clean_text[::-1]