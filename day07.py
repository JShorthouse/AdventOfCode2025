from dataclasses import dataclass

@dataclass
class Pos2D:
    x: int
    y: int

def print_map(map):
    for row in map:
        for char in row:
            print(char, end='')
        print('\n', end='')
    print('\n', end='')



with open("input/07.txt", "r") as file:
    map = []

    for line in file:
        map.append(list(line.rstrip()))

    # Find start pos
    for i in range(len(map[0])):
        if map[0][i] == 'S':
            start_pos = Pos2D(i, 0)

    print(map)
    print(start_pos)

    beam_list = [ start_pos ]
    removed_beam_count = 0
    split_count = 0

    # Simulate beams
    while len(beam_list) > 0:
        new_beam_list = []
        for beam in beam_list:
            new_y = beam.y + 1
            if new_y >= len(map):
                removed_beam_count += 1
                continue

            if map[new_y][beam.x] == '.':
                new_pos = Pos2D(beam.x, new_y)
                if not new_pos in new_beam_list:
                    new_beam_list.append(new_pos)
                    #map[new_y][beam.x] = '|'
            elif map[new_y][beam.x] == '^':
                # Found splitter, make new beams either side
                left_beam = Pos2D(beam.x - 1, new_y)
                right_beam = Pos2D(beam.x + 1, new_y)
                # Dataclass implements __eq__ which is handy. Here we are checking
                # for a position in the list that matches the X and Y, not an object
                if not left_beam in new_beam_list:
                    new_beam_list.append(left_beam)
                    #map[new_y][beam.x-1] = '|'
                if not right_beam in new_beam_list:
                    new_beam_list.append(right_beam)
                    #map[new_y][beam.x+1] = '|'

                split_count += 1
            else:
                print_map(map)
                print(beam.x, new_y)
                raise SystemExit('Found unknown character:', map[new_y][beam.x])

        beam_list = new_beam_list

    print("Part 1", split_count)

# Thoughts for Part 2: build up a list of nodes and then use depth-first search
# e.g. do an all-left path to start with, then work back up one node and do a full-left of
# that node's right path etc. Recursion is probably the easiest way to achieve this
