'''
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

 

示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        res, i, maxLen = sum(nums[:3]), 0, len(nums)
        while i < maxLen:
            startIndex, endIndex = i + 1, maxLen - 1
            while startIndex < endIndex:
                temp = sum([nums[i], nums[startIndex], nums[endIndex]])
                if temp == target:
                    return target
                else:
                    res = res if abs(target - temp) >= abs(target - res) else temp
                    if temp < target:
                        startIndex += 1
                    else:
                        endIndex -= 1
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([0, 0, 0], 1))
    print(s.threeSumClosest([0, 1, 2], 1))
    print(s.threeSumClosest([-1,2,1,-4], 1))
