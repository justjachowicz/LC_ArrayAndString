def arrayPairSum(nums: list[int]) -> int:
    sortedNums = sorted(nums)
    sumOfNums = 0

    for i in range(0, len(sortedNums), 2):
         sumOfNums += min(sortedNums[i], sortedNums[i + 1])

    return sumOfNums

print(arrayPairSum([1,4,3,2]))