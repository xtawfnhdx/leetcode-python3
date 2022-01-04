def lengthOfLongestSubstring(s: str) -> int:
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


if __name__ == "__main__":
    s = "aaa"
    ma = lengthOfLongestSubstring(s)
    print(ma)
