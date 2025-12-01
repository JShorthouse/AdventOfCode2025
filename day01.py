# I found part 2 quite tricky for a day 1 puzzle. Lots of edge cases that need to be handled
# properly. Python also handles negative integer division with '//' differently to how I expected.
# I had to walk away from the computer for a bit and come back with a hot chocolate and a 
# fresh mind. Almost resorted to just writing a brute force solution, but I managed to solve it
# in the end. Total time about 1h30m

def process_line(line):
    dir = line[0];
    number = int(line[1:])

    if dir == 'L':
        return -number
    else:
        return number


with open("input/01.txt", "r") as file:
    start_pos = 50;
    p1_count = 0;
    p2_count = 0;

    for line in file:
        move_amount = process_line(line.rstrip())

        new_position = start_pos + move_amount
        new_position_wrapped = new_position % 100

        if new_position_wrapped == 0:
            p1_count += 1

        full_loops = int(move_amount / 100)
        remainder = move_amount - (full_loops * 100)

        # We pass 0 on any full loop of the dial
        p2_count += abs(full_loops)

        # After any loops, with the remaining movement we may have wrapped past 0 or landed on 0
        # Don't run these checks if we started on 0 though, because that doesn't count as passing 0
        if start_pos != 0:
            if new_position_wrapped == 0: # We landed on 0
                p2_count += 1
            elif start_pos + remainder != new_position_wrapped: # We wrapped around 0
                p2_count += 1

        start_pos = new_position_wrapped

    print("Part 1:", p1_count)
    print("Part 2:", p2_count)
