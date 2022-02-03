from typing import List, Set, Tuple


class Node:
    def __init__(self):
        self.left: Node = None  # 0
        self.right: Node = None  # 1

    def insert(self, value: int):
        node = self

        for i in range(30, -1, -1):
            bit = (value >> i) % 2

            if bit:
                if not node.right:
                    node.right = Node()
                node = node.right
            else:
                if not node.left:
                    node.left = Node()
                node = node.left

    def get(self, value: int):
        if value == 1:
            return self.left
        if value == 0:
            return self.right

        bit_string = bin(value)[2:]
        if int(bit_string[-1]):
            return self.left.get(int(bit_string[:-1], 2))
        else:
            return self.right.get(int(bit_string[:-1], 2))


class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, bit_string):
        self.root.insert(bit_string)

    def __repr__(self):
        stack: List[Tuple[Node, str]] = [(self.root, '')]
        result_values: Set = set()
        while True:
            if not stack:
                break
            node_val = stack.pop()
            node, val = node_val

            if not node.right and not node.left:
                result_values.add(int(val, 2))
                continue

            if node.left:
                stack.append((node.left, f'{val}0'))
            if node.right:
                stack.append((node.right, f'{val}1'))
        return str(result_values)

    def find_max_xor(self, list_nums) -> int:
        result = best_res = 0
        for num in list_nums:
            node = self.root
            for i in range(30, -1, -1):
                if (num >> i) % 2:
                    if node.left:
                        node = node.left
                        result |= (1 << i)
                    else:
                        node = node.right
                else:
                    if node.right:
                        result |= (1 << i)
                        node = node.right
                    else:
                        node = node.left
            best_res = max(best_res, result)
            result = 0

        return best_res


tree = Tree()
example = [1, 2, 2 ** 32 - 1]
for i in example:
    tree.insert(i)



# nums = [3, 10, 5, 25]
nums = [1, 3, 4]
for i in nums:
    print(bin(i)[2:])
print()

L = len(bin(max(nums))) - 2
max_xor = 0
for i in range(L - 1, -1, -1):
    print(f'{i=}')
    max_xor <<= 1
    print(f'{max_xor=}')
    curr_xor = max_xor | 1
    print(f'{curr_xor=}')
    prefix = {num >> i for num in nums}
    for num in nums:
        print(f'prexif part: {num} >> {i} = {num >> i}')
    print(f'{prefix=}')
    max_xor |= any(curr_xor ^ (num >> i) in prefix for num in nums)
    for num in nums:
        print(f'{curr_xor} ^ ({num} >> {i}) = {curr_xor ^ (num >> i)}. In prefix? {curr_xor ^ (num >> i) in prefix}')
    print(f'{max_xor=}')
    print()
print(max_xor)


"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes 
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(curr_xor^p in prefixes for p in prefixes)
                    
        return max_xor
"""