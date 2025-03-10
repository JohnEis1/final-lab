import unittest
from main import *


class MyTestCase(unittest.TestCase):
# testing name function
    def test_name_checker(self):
        p1 = 'Max'
        a = player_checker(p1)
        self.assertEqual(a, True)
    def test_name_checker_2(self):
        p1 = 'rat'
        a = player_checker(p1)
        self.assertEqual(a, False)

#testing position function
    def test_position_checker(self):
        p1 = '1'
        a = position_checker(p1)
        self.assertEqual(a, True)
    def test_position_checker_2(self):
        p1 = 'rat'
        a = position_checker(p1)
        self.assertEqual(a, False)

#testing team function
    def test_team_checker(self):
        p1 = 'Lakers'
        a = team_checker(p1)
        self.assertEqual(a, True)
    def test_team_checker_2(self):
        p1 = 'rat'
        a = team_checker(p1)
        self.assertEqual(a, False)
#testing position_comparison_id
    def test_position_comparison_id(self):
        guy = Player('Max','1')
        team = 'Lakers'
        a = position_comparison_id(guy,team)
        self.assertEqual(a, ['Bowie'])
    def test_position_comparison_id_2(self):
        guy = Player('Max','1')
        team = 'rat'
        a = position_comparison_id(guy,team)
        self.assertEqual(a, [])

# testing Swap
    def test_swapping(self):
        p1 = Player('Max','1')
        team = 'Lakers'
        a = swaps(p1, team)
        self.assertEqual(a, 3)

    def test_not_swapping(self):
        p1 = Player('Max','5')
        team = 'Lakers'
        a = swaps(p1, team)
        self.assertEqual(a, None)

    def test_name_error(self):
        p1 = Player('rat', '5')
        team = 'Lakers'
        a = swaps(p1, team)
        self.assertEqual(a, False)
    def test_name_no_error(self):
        p1 = Player('Max', '5')
        team = 'Lakers'
        a = swaps(p1, team)
        self.assertEqual(a, True)

    def test_team_error(self):
        p1 = Player('Max', '5')
        team = 'rat'
        a = swaps(p1, team)
        self.assertEqual(a, False)

    def test_position_error(self):
        p1 = Player('Max', '200000')
        team = 'Warriors'
        a = swaps(p1, team)
        self.assertEqual(a, False)


if __name__ == '__main__':
    unittest.main()
