def plusOne(digits: list[int]) -> list[int]:
    digits = digits[::-1]
    isNine = True
    i = 0

    while isNine:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
                i += 1
            else:
                digits[i] += 1
                isNine = False
        else:
            digits.append(1)
            isNine = False
    return digits[::-1]

print(plusOne([9,9]))
