def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    right = len(s) - 1
    left = 0

    for i in range(len(s)):
        while left != right and left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return s




mystr = ["H","a","n","n","a","h"]
print(reverseString(mystr))