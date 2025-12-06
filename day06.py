# Part 1 was fairly simple, completed in 20 mins. Part 2 doesn't look too tricky
# but I don't want to spend another hour or so of the afternoon completing it now.
# Will probably come back and finish this one off later in the month

from dataclasses import dataclass

@dataclass
class Equation:
    numbers: list[int]
    operand: str = '?'

with open("input/06.txt", "r") as file:
    parsing_numbers = True

    equations = []

    for line in file:
        split_line = line.rstrip().split()

        if split_line[0] == '+' or split_line[0] == '*':
            for i in range(len(split_line)):
                equations[i].operand = split_line[i]
        else:
            for i in range(len(split_line)):
                if len(equations) <= i:
                    equations.append( Equation( [ int(split_line[i]) ] ) )
                else:
                    equations[i].numbers.append( int(split_line[i]) )


    # Perform calculations
    p1_total = 0

    for equation in equations:
        if equation.operand == '*':
            total = 0
            for num in equation.numbers:
                if total == 0:
                    total += num
                else:
                    total *= num
            p1_total += total
        elif equation.operand == '+':
            for num in equation.numbers:
                p1_total += num
        else:
            raise SystemExit("Found unknown operand " + equation.operand)

    print("Part 1:", p1_total)
