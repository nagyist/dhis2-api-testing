__author__ = 'Mark Polak'

from unittest import TestCase
import unittest
from equalItemsComparator import equal_items

class EqualItemsComparator(TestCase):
    def test_runs_the_function(self):
        equal_items([], [])

    def test_should_return_true_if_both_lists_are_None(self):
        self.assertTrue(equal_items(None, None))

    def test_should_return_True_for_two_empty_lists(self):
        self.assertTrue(equal_items([], []))

    def test_should_return_False_when_the_right_value_is_a_None(self):
        self.assertFalse(equal_items([], None))

    def test_should_return_False_when_the_left_value_is_a_None(self):
        self.assertFalse(equal_items(None, []))

    def test_should_return_True_for_two_equal_lists(self):
        self.assertTrue(equal_items(['Mark'], ['Mark']))

    def test_should_return_True_for_lists_with_the_same_elements_but_different_order(self):
        self.assertTrue(equal_items(['1', '2', '3'], ['3', '1', '2']))

    def test_should_return_False_for_two_unequal_lists(self):
        self.assertFalse(equal_items(['1', '2'], ['3', '1', '2']))

    def test_should_compare_normal_strings_as_unicode(self):
        self.assertTrue(equal_items(['Mark'], [u'Mark']))

    def test_should_parse_the_right_value_as_json_if_it_is_a_string(self):
        self.assertTrue(equal_items([u'Mark'], "['Mark']"))

    def test_should_return_false_if_the_right_value_can_not_be_parsed(self):
        self.assertFalse(equal_items([], '{'))

if __name__ == '__main__':
    unittest.main()
