import unittest
import tracker_main
class test_tracker_tk(unittest.TestCase):
    def test_show_help(self):
        self.assertEqual(tracker_main.showHelp(), tracker_main.cmd("?"))