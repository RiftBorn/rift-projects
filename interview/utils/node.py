"""
Node class as the basic data structure
A Node is the simplest data structure unit which has only one value and one pointed link node
Value for each node in this case is immutable
"""


class Node:

    def __init__(self, value, link_node=None):
        self._value = value
        self._link_node = link_node

    def set_link_node(self, link_node):
        """
        Resets the link node
        @param link_node: <Node> link node to be set
        """
        self._link_node = link_node

    def get_link_node(self):
        """
        Outputs the current link node
        @return: <Node> current link node
        """
        return self._link_node

    def get_value(self):
        """
        Outputs the current value
        @return:
        """
        return self._value
