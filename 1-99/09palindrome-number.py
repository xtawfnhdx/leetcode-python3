'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

进阶：你能不将整数转为字符串来解决这个问题吗？

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numlen = len(str(x))
        for i in range(numlen):
            min = int((x / (10 ** (i))) % 10)
            max = int((x / (10 ** (numlen - i - 1))) % 10)
            if min != max:
                return False
            if (i == int(numlen / 2)):
                return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(1))
    print(s.isPalindrome(0))
    print(s.isPalindrome(1221))
