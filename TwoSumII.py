def twoSum(numbers: list[int], target: int) -> list[int]:

    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                return [i + 1, j + 1]

print(twoSum([1,2,3,4,4,9,56,90], 8))


def twoSumAlternative(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        tot = numbers[l] + numbers[r]

        if tot == target:
            return [l + 1, r + 1]
        elif tot > target:
            r -= 1
        else:
            l += 1