class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x & x <= 9:
            return True
        else:
            string = str(x)
            k = 0
            i = len(string) - 1
            while k != i:
                if string[k] != string[i]:
                    return False
                k = k + 1
                i = i - 1
            return True

#A quick test
obj = Solution()
x1 = 121
x2 = -121
x3 = 10
print(obj.isPalindrome(x1))
print(obj.isPalindrome(x2))
print(obj.isPalindrome(x3))