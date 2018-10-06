from a2 import *  # * means everything
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

    def test_no_prints(self):
        self.assertFalse('print' in a2.Female.set_by_pos.__code__.co_names,
                         'print() function found in set_by_pos')


class TestGetByPos(unittest.TestCase):

    def test_01_get_returns_pos(self):
        subject1 = Female('test_subject_1')
        subject1.set_by_pos(1, 5, 'AT')
        result = subject1.get_by_pos(1, 5)
        expected = 'AT'
        self.assertEqual(result, expected, 'The chromosome is not the same')

    def test_02_get_raises_position_error(self):
        subject = Female('test_subject_2')
        subject.set_by_pos(1, 5, 'AT')
        assertRaises(PositionError, get_by_pos, 2, 5, 'AT')

    def test_03_get_raises_pair_error(self):
        subject = Female('test_subject_3')
        subject.set_by_pos(1, 5, 'AT')
        assertRaises(PairError, get_by_pos, 1, 10, 'AT')

    def test_no_prints(self):
        self.assertFalse('print' in a2.Female.get_by_pos.__code__.co_names,
                         'print() function found in get_by_pos')


class TestSetMarker(unittest.TestCase):
    ''' this class tests set marker'''
    def test_01_sets_marker_at_a_set_pos(self):
        subject = Female('123')
        subject.set_by_pos(1, 20, 'CG')
        result_dict = subject.set_marker('marker1', 1, 20)
        expected_dict = None
        self.assertEqual(result_dict, expected_dict,
                         'Marker has not been set properly when it is set at \
                         an already set position')

    def test_02_sets_marker_at_a_new_position(self):
        subject = Female('123')
        result_dict = subject.set_marker('marker1', 1, 20)
        expected_dict = None
        self.assertEqual(result_dict, expected_dict,
                         'Marker has not been set properly when set at a new \
                         position')

    def test_no_prints(self):
        self.assertFalse('print' in a2.Female.set_marker.__code__.co_names,
                         'print() function found in set_marker')


class TestSetByMarker(unittest.TestCase):
    ''' this tests set_by_marker '''
    def test_01_set_by_marker_no_chromosome(self):
        subject = Female('123')
        # when there is no chromosome set at pair-position
        subject.set_marker('marker1', 1, 20)
        result_dict = subject.set_by_marker('marker1', 'AC')
        expected_dict = None
        self.assertEqual(result_dict, expected_dict, 'marker should have \
                         added a new chromosome')

    def test_02_set_by_marker_replace_stored_chromosome(self):
        subject = Female('123')
        subject.set_by_pos(1, 20, 'GT')
        subject.set_marker('marker1', 1, 20)
        # should replace GT to AC
        result_dict = subject.set_by_marker('marker1', 'AC')
        expected_dict = None
        self.assertEqual(result_dict, expected_dict, 'marker should have \
                         replaced the old chromosome')

    def test_03_marker_not_set(self):
        subject = Female('123')
        # when there is no chromosome set at pair-position
        assertRaises(MarkerError, set_by_marker, 'marker1', 'AC')

    def test_no_prints(self):
        self.assertFalse('print' in a2.Female.set_by_marker.__code__.co_names,
                         'print() function found in set_by_marker()')


class TestGetByMarker(unittest.TestCase):
    ''' tests get by marker '''
    def test_01_marker_set_no_chromosome(self):
        subject = Female('123')
        subject.set_marker('marker1', 1, 20)
        subject.set_by_marker('marker1', 'AC')
        result = subject.get_by_marker('marker1')
        expected = 'AC'
        self.assertEqual(result, expected, 'method does not return the stored \
                         value')

    def test_02_marker_set_a_chromosome(self):
        subject = Female('123')
        subject.set_by_pos(1, 20, 'GT')
        subject.set_marker('marker1', 1, 20)
        # should replace GT to AC
        subject.set_by_marker('marker1', 'AC')
        result = subject.get_by_marker('marker')
        expected = 'AC'
        self.assertEqual(result, expected, 'method does not overwrite the \
                         previously stored value')

    def test_03_marker_not_set(self):
        subject = Female('123')
        # when there is no chromosome set at pair-position
        assertRaises(MarkerError, get_by_marker, 'marker1')

    def test_no_prints(self):
        self.assertFalse('print' in a2.Female.get_by_marker.__code__.co_names,
                         'print() function found in get_by_marker()')

if(__name__ == "__main__"):
    unittest.main(exit=False)
