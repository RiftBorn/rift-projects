"""
Linked List class
"""
from interview.utils.node import Node


class LinkedList:

    def __init__(self, value=None):
        self._head_node = Node(value=value)

    def get_head_node(self):
        """
        Gets the first node of the linked list
        @return: <Node> fist node
        """
        return self._head_node

    def insert_beginning(self, new_value):
        """
        Inserts the new node with new value to the beginning of the linked list
        @param new_value: value of the inserting new node
        """
        new_node = Node(value=new_value, link_node=self._head_node)
        self._head_node = new_node

    def stringify_list(self):
        """
        Appends values of each node to a string separated by line
        @return: <str> appended string
        """
        current = self._head_node
        result_string = ''
        while current:
            result_string += str(current.get_value()) + '\n'
            current = current.get_link_node()
        return result_string
