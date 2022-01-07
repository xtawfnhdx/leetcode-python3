# 最普通的依次遍历
def lengthOfLongestSubstringOld(self, s: str) -> int:
    if (not s or len(s) == 0):
        return 0
    max, start, end = 0, 0, 0
    ind = []
    while (start <= len(s) - 1 and end <= len(s) - 1):
        if (s[end] in ind):
            max = len(ind) if len(ind) > max else max
            start += 1
            end = start
            ind.clear()
            if (end >= len(s) - 1):
                break
        else:
            ind.append(s[end])
            if (end >= len(s) - 1):
                max = len(ind) if len(ind) > max else max
                break
            end += 1
    return max

#修改后的滑动窗口遍历
def lengthOfLongestSubstring(s: str) -> int:
    if (not s or len(s) == 0):
        return 0
    max, start, end = 0, 0, 0
    ind = []
    while (start <= len(s) - 1 and end <= len(s) - 1):
        if (s[end] in ind):
            max = len(ind) if len(ind) > max else max

            index = ind.index(s[end]) + 1
            ind = ind[index:]
            start = start + index

            ind.append(s[end])
            end += 1
        else:
            ind.append(s[end])
            end += 1

        if (end > len(s) - 1):
            max = len(ind) if len(ind) > max else max
            break

    return max


if __name__ == "__main__":
    s = "abcb"
    ma = lengthOfLongestSubstring(s)
    print(ma)
