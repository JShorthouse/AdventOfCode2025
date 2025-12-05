from dataclasses import dataclass
import copy

class MinMax:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __repr__(self):
        return "Range(%s, %s)" % (self.min, self.max)

with open("input/05.txt", "r") as file:
    ranges = []

    p1_total = 0

    parsing_ranges = True
    for line in file:
        line = line.rstrip()
        if parsing_ranges:
            if line == "":
                parsing_ranges = False
            else:
                minmax = line.split('-')
                ranges.append(MinMax(int(minmax[0]), int(minmax[1])))
        else:
            num = int(line)
            for cur_range in ranges:
                if num >= cur_range.min and num <= cur_range.max:
                    p1_total += 1
                    break

    print("Part 1:", p1_total)


    # Find non-overlaping ranges by sorting by range minimum and then building up a new list
    # If minimum of current range fits within the last range then just extend the last range
    ranges.sort(key=lambda x: x.min)

    unique_ranges = []

    unique_ranges.append(copy.deepcopy(ranges[0]))

    for i in range(1, len(ranges)):
        cur_range = ranges[i]
        last_range = unique_ranges[len(unique_ranges)-1]

        if cur_range.min >= last_range.min and cur_range.min <= last_range.max:
            # Overlapping ranges, append one to the other
            if cur_range.max > last_range.max:
                last_range.max = cur_range.max
        else:
            unique_ranges.append(copy.deepcopy(cur_range))

    total = 0
    for cur_range in unique_ranges:
        total += (cur_range.max - cur_range.min) + 1

    print("Part 2:", total)