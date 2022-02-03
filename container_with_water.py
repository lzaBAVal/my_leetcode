def maxWater(heights: list):
    max_water = 0
    start, end = 0, len(heights) - 1

    while start < end:
        print(f'start: {start}, end: {end}\n{heights[start]}, {heights[end]}')
        curr = min(heights[start], heights[end]) * (end - start)
        print(f'{curr=}')
        max_water = max(max_water, curr)
        print()

        if heights[start] > heights[end]:
            end -= 1
        else:
            start += 1

    return max_water


# l_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
l_height = [1, 2, 3, 4, 4, 3, 2, 1]

print(maxWater(l_height))
