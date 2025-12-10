from dataclasses import dataclass

@dataclass
class Pos2D:
    x: int
    y: int

def calculate_area(p1, p2):
    return (abs(p1.x - p2.x)+1) * (abs(p1.y - p2.y)+1)


with open("input/09.txt", "r") as file:
    points = []

    for line in file:
        split_line = line.rstrip().split(',')
        points.append(Pos2D( int(split_line[0]), int(split_line[1]) ))

    area_dict = {}

    for i in range(0, len(points)-1):
        for j in range(i+1, len(points)):

            # Store a map of distances with the key i-j
            # i and j are indexes into points list, i will always be the smaller of the two numbers
            # That is, the index for a pair between 5 and 7 will be stored as 5-7, there will not be a 7-5
            area_dict[str(i) + "-" + str(j)] = calculate_area(points[i], points[j])

    sorted_areas = sorted(area_dict.items(), key=lambda item: item[1])

    print("Largest area:", sorted_areas[len(sorted_areas)-1][1])


