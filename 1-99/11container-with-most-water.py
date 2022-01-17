'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def maxAreaOld(self, height: List[int]) -> int:
        '''
        会超时，不是最好算法
        :param height:
        :return:
        '''
        max = 0
        for i in range(len(height)):
            for j in range(len(height)):
                sum = (j - i) * (height[i] if height[i] <= height[j] else height[j])
                max = sum if sum >= max else max
        return max

    def maxArea(self, height: List[int]) -> int:
        '''
        使用双指针提升性能
        :param height:
        :return:
        '''
        start, sum, end = 0, 0, len(height) - 1
        while True:
            sum = max(sum, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            if start == end:
                break
        return sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([1, 1]))
    print(s.maxArea([4, 3, 2, 1, 4]))
    print(s.maxArea([1, 2, 1]))
