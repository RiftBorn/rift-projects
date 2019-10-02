from interview.utils.linked_lists import LinkedList
from interview.utils.node import Node
import unittest


class TestlinkedList(unittest.TestCase):

    def setUp(self):
        self.example_value_1 = 'example value 1'
        self.example_value_2 = 'example value 2'
        self.example_value_3 = 'example value 3'
        self.example_value_list = [1, '2', 3.0, 4]
        self.example_node_1 = Node(value=self.example_value_1)
        self.example_node_2 = Node(value=self.example_value_2)
        self.example_node_3 = Node(value=self.example_value_3)
        self.example_linked_list = LinkedList(self.example_value_1)
        self.example_stringified_list = 'example value 2\nexample value 1\n'
        self.example_stringified_list_2 = 'example value 1\nexample value 2\n'
        self.example_stringified_list_3 = '1\n2\n3.0\n4\n'
        self.example_empty_list = LinkedList()
        self.example_empty_list._head_node = None
        pass

    def test_add_value_to_the_end(self):
        """
        test interview.utils.linked_list :: LinkedList :: add_value_to_the_end
        """
        expected = self.example_stringified_list_2
        self.example_linked_list.add_value_to_the_end(self.example_value_2)
        returned = self.example_linked_list.stringify_list()
        self.assertEqual(expected, returned)

        # when there is no head node
        expected = self.example_value_1 + '\n'
        self.example_empty_list.add_value_to_the_end(self.example_value_1)
        returned = self.example_empty_list.stringify_list()
        self.assertEqual(expected, returned)

    def test_construct_from_list(self):
        """
        test interview.utils.linked_list :: LinkedList :: _construct_from_list
        """
        expected = self.example_stringified_list_3
        self.example_linked_list._construct_from_list(self.example_value_list)
        returned = self.example_linked_list.stringify_list()
        self.assertEqual(expected, returned)

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

    def test_remove_first_node_by_value(self):
        """
        test interview.utils.linked_list :: LinkedList :: remove_first_node_by_value
        """
        ref_list = ['value1', 'value2', 'value1', 'value2', 'value3', 'value3']
        tests = [{
            "value": "value1",
            "returned": "value2\nvalue1\nvalue2\nvalue3\nvalue3\n",
        }, {
            "value": "value2",
            "returned": "value1\nvalue1\nvalue2\nvalue3\nvalue3\n",
        }, {
            "value": "value3",
            "returned": "value1\nvalue2\nvalue1\nvalue2\nvalue3\n",
        }, {
            "value": "value4",
            "returned": "value1\nvalue2\nvalue1\nvalue2\nvalue3\nvalue3\n"
        }]
        for test in tests:
            value = test.get('value')
            expected = test.get('returned')
            linked_list = LinkedList(ref_list=ref_list, by_list=True)
            linked_list.remove_first_node_by_value(value)
            returned = linked_list.stringify_list()
            self.assertEqual(expected, returned)

    def test_stringify_list(self):
        """
        test interview.utils.linked_list :: LinkedList :: stringify_list
        """
        expected = self.example_stringified_list
        self.example_linked_list.insert_beginning(self.example_value_2)
        returned = self.example_linked_list.stringify_list()
        self.assertEqual(expected, returned)
