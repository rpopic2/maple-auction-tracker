import unittest
import datagen
import koreanParser
from datetime import date


class datagentest(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(25000000, koreanParser.parseNum("2500만"))
        self.assertEqual(25000, koreanParser.parseNum("2.5"))
        self.assertEqual(25000, koreanParser.parseNum("2.5만"))
        self.assertEqual(25000, koreanParser.parseNum("25000"))
        self.assertEqual(25000, koreanParser.parseNum("25,000"))
