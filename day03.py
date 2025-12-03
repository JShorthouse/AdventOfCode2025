import unittest

def find_max_pair(input):
    nums = list(map(int, input))

    # Find first number by finding highest leftmost number, up to length-1
    # [o o o X o o] o
    first_number = 0
    first_number_pos = 0
    for i in range(len(nums) - 1):
        if nums[i] > first_number:
            first_number = nums[i]
            first_number_pos = i

    # Find second number by finding highest leftmost number from after first number to end of string
    # o o o X [ o X o ]
    second_number = 0
    for i in range(first_number_pos + 1, len(nums)):
        if nums[i] > second_number:
            second_number = nums[i]


    return int(str(first_number) + str(second_number))

def find_max_N(input, n):
    nums = list(map(int, input))

    output_num = ""

    last_pos = -1

    for digit_num in range(n):
        cur_max = -1
        cur_pos = 0

        # For n digits, iterate from the last position to the end of the array, minus how many digits are left to find
        # e.g for digit 3/5 (2 digits after this one left to find)
        # o o o [ o o o o ] o o
        for i in range(last_pos + 1, len(nums) - (n - 1 - digit_num)):
            if nums[i] > cur_max:
                cur_max = nums[i]
                cur_pos = i

        output_num += str(cur_max)
        last_pos = cur_pos

    return int(output_num)



with open("input/03.txt", "r") as file:
    p1_total = 0
    p2_total = 0
    for line in file:
        p1_total += find_max_pair(line.rstrip())
        p2_total += find_max_N(line.rstrip(), 12)

    for line in file:
        p1_total += find_max_pair(line.rstrip())

    print("Part 1:", p1_total)
    print("Part 2:", p2_total)


class TestDay3(unittest.TestCase):
    def test_find_max_pair(self):
        self.assertEqual(find_max_pair("818181911112111"), 92)
        self.assertEqual(find_max_pair("987654321111111"), 98)
        self.assertEqual(find_max_pair("234234234234278"), 78)
        self.assertEqual(find_max_pair("811111111111119"), 89)

    def test_find_max_N(self):
        self.assertEqual(find_max_N("818181911112111", 2), 92)
        self.assertEqual(find_max_N("987654321111111", 2), 98)
        self.assertEqual(find_max_N("234234234234278", 2), 78)
        self.assertEqual(find_max_N("811111111111119", 2), 89)

        self.assertEqual(find_max_N("818181911112111", 12), 888911112111)
        self.assertEqual(find_max_N("987654321111111", 12), 987654321111)
        self.assertEqual(find_max_N("234234234234278", 12), 434234234278)
        self.assertEqual(find_max_N("811111111111119", 12), 811111111119)

unittest.main()
