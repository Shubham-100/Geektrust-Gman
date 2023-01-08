import unittest
from src import power

class TestPower(unittest.TestCase):
    path1 = "./sample_input/input1.txt"
    path2 = "./sample_input/input2.txt"
    path3 = "./sample_input/input3.txt"

    def testPower(self):
        p = power.Power(self.path1)
        p.readFile()
        self.assertEqual(p.calculatePower(), 155)

        p = power.Power(self.path2)
        p.readFile()
        self.assertEqual(p.calculatePower(), 90)

        p = power.Power(self.path3)
        p.readFile()
        self.assertEqual(p.calculatePower(), 110)


if __name__ == '__main__':
    unittest.main()