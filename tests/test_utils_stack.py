import unittest
from interview.utils.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.example_basic_stack = Stack()
        self.example_empty_item_stack = Stack()
        pass

    def test_has_space(self):
        """
        test interview.utils.stack :: Stack :: _has_space
        """
        # when size < limit
        self.example_basic_stack.size = 999
        returned = self.example_basic_stack._has_space()
        self.assertTrue(returned)

        # when size >= limit
        self.example_basic_stack.size = 1000
        returned = self.example_basic_stack._has_space()
        self.assertFalse(returned)

    def test_is_empty(self):
        """
        test interview.utils.stack :: Stack :: is_empty
        """
        # when stack is empty
        self.example_basic_stack.size = 0
        returned = self.example_basic_stack.is_empty()
        self.assertTrue(returned)

        # when stack is not empty
        self.example_basic_stack.size = 1
        returned = self.example_basic_stack.is_empty()
        self.assertFalse(returned)

    def test_peek(self):
        """
        test interview.utils.stack :: Stack :: peek
        """
        self.example_empty_item_stack.reset_from_list([1, 2, 3, 4, 5])
        expected = 1
        returned = self.example_empty_item_stack.peek()
        self.assertEqual(expected, returned)

        # when size = 0
        expected = None
        self.example_empty_item_stack = Stack()
        returned = self.example_empty_item_stack.peek()
        self.assertEqual(expected, returned)

    def test_pop(self):
        """
        test interview.utils.stack :: Stack :: pop
        """
        self.example_empty_item_stack.reset_from_list([1, 2, 3, 4, 5])
        expected, expected_list = 1, [2, 3, 4, 5]
        returned = self.example_empty_item_stack.pop()
        returned_list = self.example_empty_item_stack.to_list()
        self.assertEqual((expected, expected_list), (returned, returned_list))

        # when size = 0
        self.example_empty_item_stack = Stack()
        expected, expected_list = None, []
        returned = self.example_empty_item_stack.pop()
        returned_list = self.example_empty_item_stack.to_list()
        self.assertEqual((expected, expected_list), (returned, returned_list))

    def test_push(self):
        """
        test interview.utils.stack :: Stack :: push
        """
        self.example_empty_item_stack.reset_from_list([1, 2, 3, 4, 5])
        expected = [9, 1, 2, 3, 4, 5]
        self.example_empty_item_stack.push(9)
        returned = self.example_empty_item_stack.to_list()
        self.assertEqual(expected, returned)

        # when stack does not have space
        self.example_empty_item_stack.reset_from_list([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        self.example_empty_item_stack.limit = 5
        self.example_empty_item_stack.push(9)
        returned = self.example_empty_item_stack.to_list()
        self.assertEqual(expected, returned)
