import unittest
from interview.utils.node import Node


class TestNode(unittest.TestCase):

    def setUp(self):
        self.example_node = 'node_1'
        self.example_value = 'example_value'
        self.example_link_node = 'example_link_node'
        self.example_node_with_properties = Node(value=self.example_value, link_node=self.example_link_node)

    @staticmethod
    def _create_node():
        """
        Create a Node instance
        @return: <Node> Node instance
        """
        return Node('example value')

    def test_set_link_node(self):
        """
        test interview.utils.node :: Node :: set_link_node
        """
        tests = [{
            "node": self.example_node,
            "returned": self.example_node,
        }]
        for test in tests:
            node = test.get("node")
            expected = test.get("returned")
            returned_node = self._create_node()
            returned_node.set_link_node(node)
            returned = returned_node._link_node
            self.assertEqual(expected, returned)

    def test_get_link_node(self):
        """
        test interview.utils.node :: Node :: get_link_node
        """
        expected = self.example_link_node
        returned = self.example_node_with_properties.get_link_node()
        self.assertEqual(expected, returned)

    def test_get_value(self):
        """
        test interview.utils.node :: Node :: get_value
        """
        expected = self.example_value
        returned = self.example_node_with_properties.get_value()
        self.assertEqual(expected, returned)
