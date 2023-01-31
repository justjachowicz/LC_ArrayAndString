def dominantIndex(nums: list[int]) -> int:
    maxNum = max(nums)
    twiceAsBig = maxNum // 2
    for num in nums:
        if num != maxNum and num > twiceAsBig:
            return -1
    return nums.index(maxNum)


print(dominantIndex([1,2,3,4]))
