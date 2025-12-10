from dataclasses import dataclass

@dataclass
class Beam:
    x: int
    y: int
    count: int

def print_map(map):
    for row in map:
        for char in row:
            print(char, end='')
        print('\n', end='')
    print('\n', end='')


def find_beam(list, x, y):
    for beam in list:
        if beam.x == x and beam.y == y:
            return beam

    return None

with open("input/07.txt", "r") as file:
    map = []

    for line in file:
        map.append(list(line.rstrip()))

    # Find start pos
    for i in range(len(map[0])):
        if map[0][i] == 'S':
            start_pos = Beam(i, 0, 1)

    beam_list = [ start_pos ]
    finished_beams = []
    split_count = 0

    # Simulate beams
    while len(beam_list) > 0:
        new_beam_list = []
        for beam in beam_list:
            new_y = beam.y + 1
            if new_y >= len(map):
                finished_beams.append( beam )
                continue

            if map[new_y][beam.x] == '.':
                existing_beam = find_beam(new_beam_list, beam.x, new_y)
                if existing_beam is None:
                    new_beam_list.append( Beam(beam.x, new_y, beam.count ) )
                    #map[new_y][beam.x] = '|'
                else:
                    existing_beam.count += beam.count
            elif map[new_y][beam.x] == '^':
                # Found splitter, make new beams either side
                left_beam = Beam(beam.x - 1, new_y, beam.count)
                right_beam = Beam(beam.x + 1, new_y, beam.count)
                # Dataclass implements __eq__ which is handy. Here we are checking
                # for a position in the list that matches the X and Y, not an object
                existing_left = find_beam(new_beam_list, left_beam.x, left_beam.y)
                existing_right = find_beam(new_beam_list, right_beam.x, right_beam.y)
                if existing_left is None:
                    new_beam_list.append(left_beam)
                else:
                    existing_left.count += beam.count
                if existing_right is None:
                    new_beam_list.append(right_beam)
                else:
                    existing_right.count += beam.count

                split_count += 1
            else:
                print_map(map)
                print(beam.x, new_y)
                raise SystemExit('Found unknown character:', map[new_y][beam.x])

        beam_list = new_beam_list

    print("Part 1", split_count)
    print("Part 2", sum(beam.count for beam in finished_beams))
