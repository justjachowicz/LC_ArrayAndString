def plusOne(digits: list[int]) -> list[int]:
    first_str = ''
    for digit in digits:
        first_str += str(digit)

    added_numer = int(first_str) + 1
    added_string = str(added_numer)

    output_list = []
    for letter in added_string:
        output_list.append(int(letter))

    return output_list

print(plusOne([9]))
