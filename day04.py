offsets = [
    [1, 1],
    [1, 0],
    [1, -1],
    [0, 1],
    [0, -1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
]

def find_spaces_with_less_adjacent(grid, limit, target):
    num_matched = 0
    matched_positions = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != target:
                continue

            count = 0
            for offset in offsets:
                search_x = x + offset[0]
                search_y = y + offset[1]
                if search_x >= 0 and search_y >= 0 and search_x < len(grid[0]) and search_y < len(grid):
                    if grid[search_y][search_x] == target:
                        count += 1

            if count < limit:
                matched_positions.append([y, x])

    return matched_positions


def remove_spaces_from_grid(grid, position_list):
    for pos in position_list:
        grid[pos[0]][pos[1]] = "."


with open("input/04.txt", "r") as file:
    grid = []

    for line in file:
        row = list(line.rstrip())
        grid.append(row)

    print("Part 1:", len(find_spaces_with_less_adjacent(grid, 4, '@')))

    total_removed = 0
    while True:
        removable_spaces = find_spaces_with_less_adjacent(grid, 4, '@')
        if len(removable_spaces) == 0:
            break

        remove_spaces_from_grid(grid, removable_spaces)
        total_removed += len(removable_spaces)

    print("Part 2:", total_removed)