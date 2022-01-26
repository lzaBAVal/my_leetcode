from typing import List

def LSC(str1: str, str2: str, row, col, dp):
    if col-1 == -1 or row-1 == -1:
        return 0

    if dp[row-1][col-1] != -1:
        print(f'was here: row: {row-1}, col: {col-1}')
        return dp[row-1][col-1]

    if list(str1)[col-1] == list(str2)[row-1]:
        print(f'{list(str2)[row-1]}:{row-1} = {list(str1)[col-1]}:{col-1}')
        dp[row-1][col-1] = 1 + LSC(str1, str2, row-1, col-1, dp)
        print_dp(dp)
        return dp[row-1][col-1]
    else:
        up = LSC(str1, str2, row-1, col, dp)
        left = LSC(str1, str2, row, col-1, dp)
        print(f'up: row = {row-2}, col = {col-1}, up={up}', end='; ')
        print(f'left: row = {row-1}, col = {col-2}, left={left}')
        dp[row-1][col-1] = max(up, left)
        print(f'dp[{row-1}][{col-1}] = {dp[row-1][col-1]}')
        print_dp(dp)
        return dp[row-1][col-1]


def get_dp(cols: int, rows: int) -> List[List[int]]:
    return [[-1 for _ in range(cols)] for _ in range(rows)]


def print_dp(dp: List[List[int]]) -> None:
    columns = [f' {col} ' for col in range(len(dp[0]))]
    result = f'\t{str(" ".join(columns))}\n'
    for row in range(len(dp)):
        result += f'{row}\t'
        for col in range(len(dp[row])):
            result += f'{dp[row][col]}\t'
        result += '\n'
    print(result)


str1 = 'aggtab'
str2 = 'gxtxayb'

col = len(str1)
row = len(str2)

dp = get_dp(col, row)
print_dp(dp)

print(LSC(str1, str2, row, col, dp))


