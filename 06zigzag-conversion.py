'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
 
示例 1：
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        interval, i, j = (numRows - 1) * 2, 0, 0
        temp = []

        if numRows == 1:
            return s

        while True:
            index = i * interval + j
            # 反向计算数据的位置（非首末行）
            index2 = (i + 1) * interval - j
            if index < len(s):
                if index != index2 and j > 0 and j < numRows - 1:
                    temp.append(s[index])
                    # 不是第一行与最后一行，需要多增加一个数据进去
                    if index2 < len(s):
                        temp.append(s[index2])
                else:
                    temp.append(s[index])
                i += 1
            else:
                i = 0
                j += 1
            if j >= numRows:
                break

        return "".join(temp)


if __name__ == "__main__":
    s = Solution()
    ss = s.convert("Abc", 2)
    print(ss)
