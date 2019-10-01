from interview.utils.linked_lists import LinkedList
from interview.utils.node import Node
import unittest


class TestlinkedList(unittest.TestCase):

    def setUp(self):
        self.example_value_1 = 'example value 1'
        self.example_value_2 = 'example value 2'
        self.example_value_3 = 'example value 3'
        self.example_node_1 = Node(value=self.example_value_1)
        self.example_node_2 = Node(value=self.example_value_2)
        self.example_node_3 = Node(value=self.example_value_3)
        self.example_linked_list = LinkedList(self.example_value_1)
        self.example_stringified_list = 'example value 2\nexample value 1\n'
        pass

    def test_get_head_node(self):
        """
        test interview.utils.linked_list :: LinkedList :: get_head_node
        """
        expected = self.example_value_1
        returned = self.example_linked_list.get_head_node().get_value()
        self.assertEqual(expected, returned)

    def test_insert_beginning(self):
        """
        test interview.utils.linked_list :: LinkedList :: insert_beginning
        """
        expected = self.example_value_2
        self.example_linked_list.insert_beginning(self.example_value_2)
        returned = self.example_linked_list._head_node.get_value()
        self.assertEqual(expected, returned)

    def test_stringify_list(self):
        """
        test interview.utils.linked_list :: LinkedList :: stringify_list
        """
        expected = self.example_stringified_list
        self.example_linked_list.insert_beginning(self.example_value_2)
        returned = self.example_linked_list.stringify_list()
        self.assertEqual(expected, returned)
