from typing import List

l = [1, 2, 3, 4, 5]
target = 9


# ~4.5sec and ~15Mb
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_a in range(0, len(nums) - 1):
            for num_b in range(num_a + 1, len(nums)):
                if num_a + num_b == target:
                    return [num_a, num_b]


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i


def sumOfSquareNums(c:int) -> bool:
    l = [i ** 2 for i in range(0, c + 1)]
    d = []
    for n in l:
        d.append(n)
        if c - n in d:
            return True
    return False

print(twoSum(nums=l, target=target))
