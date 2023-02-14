def strStr(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)

    for window_start in range(n - m + 1):
        for i in range(m):
            if needle[i] != haystack[window_start + 1]:
                break
            if i == m - 1:
                return window_start
    return -1