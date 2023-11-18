def find_seven_dwarfs(heights):
    total_height = sum(heights)
    for i in range(9):
        for j in range(i + 1, 9):
            if total_height - heights[i] - heights[j] == 100:
                result = [h for idx, h in enumerate(heights) if idx != i and idx != j]
                result.sort()
                return result

heights = [int(input()) for _ in range(9)]

result = find_seven_dwarfs(heights)
for h in result:
    print(h)
