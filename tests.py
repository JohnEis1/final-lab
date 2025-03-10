import unittest
from main import *


class MyTestCase(unittest.TestCase):


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
