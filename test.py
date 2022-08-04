import unittest
import datagen
import koreanParser
from datetime import date


class parsertest(unittest.TestCase):
    def test_parse_number(self):
        self.assertEqual(25000000, koreanParser.parseNum("2500만"))
        self.assertEqual(25000, koreanParser.parseNum("2.5"))
        self.assertEqual(25000, koreanParser.parseNum("2.5만"))
        self.assertEqual(25000, koreanParser.parseNum("25000"))
        self.assertEqual(25000, koreanParser.parseNum("25,000"))
        
    def test_parse_command(self):
        self.assertEqual(["아무개아이템", "2.5만"], koreanParser.parseCmd("아무개아이템 2.5만"))
        self.assertEqual(["레인디어의창", "2.5만"], koreanParser.parseCmd("레인디어의창 2.5만"))


class test_tracker_main(unittest.TestCase):
    pass
