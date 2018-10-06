from a2 import *
import unittest


class TestSetByPos(unittest.TestCase):

    def test_01_set_returns_none(self):
        subject1 = Female('test_subject_1')
        # try setting by position
        result = subject1.set_by_pos(1, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")


    def test_02_set_replace_previous_element(self):
        subject2 = Female('test_subject_2')
        temp_result = subject2.set_by_pos(1, 5, 'GC')
        result = subject2.set_by_pos(1, 5, 'AT')
        expected = None
        self.assertEqual(result, expected,
                         'The value at 1-5 should be overwritten')

    def test_03_set_gets_empty_string(self):
        subject1 = Female('test_subject_1')
        # try setting by position
        result = subject1.set_by_pos(1, 5, ' ')
        expected = None
        self.assertEqual(result, expected, 'Blank spaces are still strings')

if(__name__ == "__main__"):
    unittest.main(exit=False)