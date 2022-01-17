class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 将左右指针移动到原有相同的那里
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            # 某一个点的回文长度
            left1, right1 = self.expandAroundCenter(s, i, i)

            # 挨着两个字母一样的回文长度
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        # 不包括end，所以END要加一
        return s[start:end + 1]


if __name__ == '__main__':
    c =Solution()
    ss=c.longestPalindrome('cbbd')
    print(ss)
