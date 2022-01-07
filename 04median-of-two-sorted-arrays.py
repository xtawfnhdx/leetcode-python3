from typing import List


def findMedianSortedArraysOld(nums1: List[int], nums2: List[int]) -> float:
    temp, x, y = [], 0, 0

    while x <= len(nums1) and y <= len(nums2):
        if x == len(nums1) or y == len(nums2):
            if x != len(nums1):
                temp = nums1[x:] if not temp else temp + nums1[x:]
            elif y != len(nums2):
                temp = nums2[y:] if not temp else temp + nums2[y:]
            else:
                pass
            break

        if nums1[x] < nums2[y]:
            temp.append(nums1[x])
            x += 1
        elif nums1[x] == nums2[y]:
            temp.append(nums1[x])
            temp.append(nums2[y])
            x += 1
            y += 1
        else:
            temp.append(nums2[y])
            y += 1
    if not temp:
        return float(0)
    if (len(temp) % 2 == 0):
        if (len(temp) % 2 == 0):
            index = int(len(temp) / 2)
            return float(temp[index - 1] + temp[index]) / 2
        else:
            index = int(len(temp) / 2)
            return float(temp[index])


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # if (len(nums1) < len(nums2)):
    #     findMedianSortedArrays(nums2, nums1)

    if not nums1 and not nums2:
        return 0
    # 基数
    isBase = int((len(nums1) + len(nums2)) % 2) == 1
    minIndex = int((len(nums1) + len(nums2)) / 2) if isBase else int((len(nums1) + len(nums2)) / 2) - 1

    while True:
        tempIndex = int(minIndex / 2)
        if not nums1:
            return float(nums2[minIndex]) if isBase == True else \
                float((nums2[minIndex] + nums2[minIndex + 1]) / 2)
        if not nums2:
            return float(nums1[minIndex]) if isBase == True else \
                float((nums1[minIndex] + nums1[minIndex + 1]) / 2)

        if (minIndex == 0):
            if (isBase == True):
                return nums1[0] if nums1[0] <= nums2[0] else nums2[0]
            else:
                v1 = nums1[0] + nums2[0]
                v2 = nums1[0] + nums1[1] if len(nums1) > 1 else v1+1
                v3 = nums2[0] + nums2[1] if len(nums2) > 1 else v1+1
                return float(min(v1, v2, v3) / 2)

        v1 = nums1[tempIndex if len(nums1) > tempIndex else len(nums1) - 1]
        v2 = nums2[tempIndex if len(nums2) > tempIndex else len(nums2) - 1]
        ind = 0
        if v1 <= v2:
            ind = tempIndex + 1 if len(nums1) > tempIndex else len(nums1)
            nums1 = nums1[ind:]
        else:
            ind = tempIndex + 1 if len(nums2) > tempIndex else len(nums2)
            nums2 = nums2[ind:]
        minIndex = minIndex - ind


if __name__ == "__main__":
    # t1 = [1, 3]
    # t2 = [2]
    # x1 = findMedianSortedArrays(t1, t2)
    # print(x1)

    # a1 = [1, 2, 3, 3, 3]
    # a2 = [3, 4]

    a1 =[0,0,0,0,0]
    a2 = [-1,0,0,0,0,0,1]
    y1 = findMedianSortedArrays(a1, a2)
    print(y1)
