import unittest

from character_create.create_character import create_character


class TestCreateCharacter(unittest.TestCase):

    # Test case 1: Valid character with stats summing to 7
    def test_valid_input(self):
        result = create_character('ren', 4, 2, 1)
        expected = '''ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○'''
        self.assertEqual(result, expected)

    # Test case 2: Invalid name (not a string)
    def test_invalid_name_non_string(self):
        result = create_character(123, 4, 2, 1)
        self.assertEqual(result, 'The character name should be a string')

    # Test case 3: Invalid name (empty string)
    def test_invalid_name_empty(self):
        result = create_character('', 4, 2, 1)
        self.assertEqual(result, 'The character should have a name')

    # Test case 4: Invalid name (longer than 10 characters)
    def test_invalid_name_too_long(self):
        result = create_character('Alicia_12345', 4, 2, 1)
        self.assertEqual(result, 'The character name is too long')

    # Test case 5: Name is not too long (should not say it's too long)
    def test_valid_name_length(self):
        result = create_character('Alice', 4, 2, 1)
        self.assertNotEqual(result, 'The character name is too long')

    # Test case 6: Invalid name (contains spaces)
    def test_invalid_name_with_space(self):
        result = create_character('John Doe', 4, 2, 1)
        self.assertEqual(result, 'The character name should not contain spaces')

    # Test case 7: Invalid stats (non-integer)
    def test_invalid_stats_non_integer(self):
        result = create_character('Bob', '3', 2, 1)
        self.assertEqual(result, 'All stats should be integers')

    # Test case 8: Invalid stats (less than 1)
    def test_invalid_stats_less_than_1(self):
        result = create_character('Charlie', 0, 2, 5)
        self.assertEqual(result, 'All stats should be no less than 1 and no more than 4')

    # Test case 9: Invalid stats (greater than 4)
    def test_invalid_stats_more_than_4(self):
        result = create_character('David', 5, 2, 0)
        self.assertEqual(result, 'All stats should be no less than 1 and no more than 4')

    # Test case 10: Stats sum not equal to 7
    def test_invalid_stats_sum_not_7(self):
        result = create_character('Eva', 4, 4, 1)
        self.assertEqual(result, 'The character should start with 7 points')

    # Test case 11: Valid stats and valid name
    def test_valid_values(self):
        result = create_character('ren', 4, 2, 1)
        self.assertEqual(result, '''ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○''')

    # Test case 12: Validate the function's behavior with valid input
    def test_valid_input_check(self):
        result = create_character('Zoe', 2, 3, 2)
        expected = '''Zoe
STR ●●○○○○○○○○
INT ●●●○○○○○○○
CHA ●●○○○○○○○○'''
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
