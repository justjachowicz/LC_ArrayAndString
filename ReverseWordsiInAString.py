def reverseWords(s: str) -> str:
    new_string = s.split()[::-1]
    joined_string = " ".join(new_string)

    reversed_letters = joined_string[::-1]

    return reversed_letters

print(reverseWords("Let's take LeetCode contest"))
