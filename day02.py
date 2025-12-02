# I spent ages on part 1 because I didn't read the bit about only matching 2
# occurences of the pattern and so I accidentally solved part 2 and then wondered
# why my solution didn't match the sample input...
# At least after I got over my frustration and got a working answer for part 1
# it took me only a minute to get both stars! Total time about 1h30m

import unittest

def has_two_pattern(id):
    id = str(id)

    if len(id) == 1:
        return False

    middle = len(id) // 2

    return id[0:middle] == id[middle:]

def has_any_pattern(id):
    id = str(id)

    if len(id) == 1:
        return False

    middle = len(id) // 2

    # Check all possible patterns, up to length of middle
    for i in range(middle):
        pattern = id[0:i+1]

        if len(id) % len(pattern) != 0:
            continue

        pattern_repeats = True
        base = 0
        while base < len(id) and pattern_repeats:
            for j in range(len(pattern)):
                if pattern[j] != id[base + j]:
                    pattern_repeats = False
                    break

            base += len(pattern)

        if pattern_repeats:
            return True

    return False

def get_invalid_ids_for_range(rang, pattern_func):
    splt = rang.split('-')
    start = splt[0]
    end = splt[1]

    count = 0
    ids = []

    for num in range(int(start), int(end)+1):
        if pattern_func(num):
            count += 1
            ids.append(num)

    return ids


with open("input/02.txt", "r") as file:
    p1_total = 0
    p2_total = 0
    for line in file:
        for input_range in line.rstrip().split(','):
            p1_total += sum(get_invalid_ids_for_range(input_range, has_two_pattern))
            p2_total += sum(get_invalid_ids_for_range(input_range, has_any_pattern))

    print("Part 1:", p1_total)
    print("Part 2:", p2_total)


class TestCheckForPattern(unittest.TestCase):
    def test_valid_two_patterns(self):
        self.assertTrue(has_two_pattern(1010))
        self.assertTrue(has_two_pattern(11))
        self.assertTrue(has_two_pattern(9999))
        self.assertTrue(has_two_pattern(256256))
        self.assertTrue(has_two_pattern(256256256256))

    def test_valid_any_patterns(self):
        self.assertTrue(has_any_pattern(1010))
        self.assertTrue(has_any_pattern(11))
        self.assertTrue(has_any_pattern(256256))
        self.assertTrue(has_any_pattern(256256256))
        self.assertTrue(has_any_pattern(256256256256))
        self.assertTrue(has_any_pattern(12345671234567))

    def test_invalid_two_patterns(self):
        self.assertFalse(has_two_pattern(256256256))
        self.assertFalse(has_two_pattern(111))
        self.assertFalse(has_two_pattern(101010))
        self.assertFalse(has_two_pattern(12341234123412341234))
    
    def test_invalid_any_patterns(self):
        self.assertFalse(has_two_pattern(1234))
        self.assertFalse(has_two_pattern(10101))
        self.assertFalse(has_two_pattern(12121))
        self.assertFalse(has_two_pattern(12))
        self.assertFalse(has_two_pattern(256256251))
        self.assertFalse(has_two_pattern(156256256))
        self.assertFalse(has_two_pattern(1011))
        self.assertFalse(has_two_pattern(1001))

class TestCountPatternsForRange(unittest.TestCase):
    def two_pattern(self):
        self.assertEqual(len(get_invalid_ids_for_range("11-22"), has_two_pattern), 2)
        self.assertEqual(len(get_invalid_ids_for_range("95-115"), has_two_pattern), 1)
        self.assertEqual(len(get_invalid_ids_for_range("998-1012"), has_two_pattern), 1)
        self.assertEqual(len(get_invalid_ids_for_range("1188511880-1188511890"), has_two_pattern), 1)
        self.assertEqual(len(get_invalid_ids_for_range("222220-222224"), has_two_pattern), 1)
        self.assertEqual(len(get_invalid_ids_for_range("1698522-1698528"), has_two_pattern), 0)
        self.assertEqual(len(get_invalid_ids_for_range("446443-446449"), has_two_pattern), 1)

    def any_pattern(self):
        self.assertEqual(len(get_invalid_ids_for_range("11-22"), has_any_pattern), 2)
        self.assertEqual(len(get_invalid_ids_for_range("95-115"), has_any_pattern), 2)
        self.assertEqual(len(get_invalid_ids_for_range("998-1012"), has_any_pattern), 2)
        self.assertEqual(len(get_invalid_ids_for_range("1188511880-1188511890"), has_any_pattern), 1)
        self.assertEqual(len(get_invalid_ids_for_range("222220-222224"), has_any_pattern), 1)
        self.assertEqual(len(get_invalid_ids_for_range("1698522-1698528"), has_any_pattern), 0)
        self.assertEqual(len(get_invalid_ids_for_range("446443-446449"), has_any_pattern), 1)

unittest.main();
