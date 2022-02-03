def get_palindrom(s: str, start: int, end: int):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return start + 1, end - 1


def palindromic_alphabet(s: str):
    max_len = 0
    max_substring = ''
    for i in range(len(s)):
        start, end = get_palindrom(s, i, i)
        if end + 1 - start > max_len:
            max_len = end + 1 - start
            max_substring = s[start:end + 1]
        start, end = get_palindrom(s, i, i + 1)
        if end + 1 - start > max_len:
            max_len = end + 1 - start
            max_substring = s[start:end+1]
    return max_substring


print(palindromic_alphabet('awamuecamyajqjqjayawvavwtvdsrv'))
