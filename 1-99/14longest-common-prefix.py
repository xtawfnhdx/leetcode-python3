'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenList = [len(x) for x in strs]
        minIndex = lenList.index(min(lenList))
        minvalue = strs[minIndex]

        for i in range(len(strs)):
            minvalue = self.getMinStr(strs[i], minvalue)
            if len(minvalue) == 0:
                return ""
        return minvalue

    def getMinStr(self, str1: str, str2: str) -> str:
        res = []
        length = len(str1) if len(str1) < len(str2) else len(str2)
        for i in range(length):
            if str1[i] == str2[i]:
                res.append(str1[i])
            else:
                return "".join(res)
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["cir","car"]))
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
