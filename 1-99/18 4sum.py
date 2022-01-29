'''
给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]（若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 题解方法与三重循环类似
        listlen = len(nums)
        if listlen < 4:
            return []
        nums.sort()
        res = []
        for i in range(listlen - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[listlen - 1] + nums[listlen - 2] + nums[listlen - 3] < target:
                continue
            for j in range(i + 1, listlen - 2):
                if j > i + 2 and nums[j] == nums[j - 1]:
                    continue
                startIndex, endIndex = j + 1, listlen - 1
                while startIndex < endIndex:
                    if nums[i] + nums[j] + nums[startIndex] + nums[endIndex] < target:
                        startIndex += 1
                    elif nums[i] + nums[j] + nums[startIndex] + nums[endIndex] > target:
                        endIndex -= 1
                    else:
                        temp = [nums[i], nums[j], nums[startIndex], nums[endIndex]]
                        if temp not in res:
                            res.append(temp)
                        startIndex += 1
                        endIndex -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([0, 0, 0, 0], 0))
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([2, 2, 2, 2, 2], 8))
