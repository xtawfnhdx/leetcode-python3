'''
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def isValid(self, s: str) -> bool:
        leftBracket=["(","{","["]
        rightBrakcet=[")","}","]"]
        tempStack=[]
        for temp in s:
            if temp in ["(","{","["]:
                tempStack.append(temp)
            else :
                if len(tempStack)==0 or leftBracket.index(tempStack.pop())!=rightBrakcet.index(temp):
                    return False
        return True if len(tempStack)==0 else False
if __name__=="__main__":
    s=Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("{"))
    print(s.isValid("]"))