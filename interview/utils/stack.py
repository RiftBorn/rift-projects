"""
Stack class with node
"""

from .node import Node

DEFAULT_LIMIT = 1000


class Stack:

    def __init__(self, limit=DEFAULT_LIMIT):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def _has_space(self):
        """
        Returns whether the stack has space
        @return: <bool> whether the stack has space
        """
        return self.limit > self.size

    def is_empty(self):
        """
        Returns whether the stack is empty
        @return: <bool> whether the stack is empty
        """
        return self.size == 0

    def peek(self):
        """
        Returns the top value of the stack
        @return: top value
        """
        if self.size == 0:
            return None
        return self.top_item.get_value()

    def pop(self):
        """
        Pops the top item of the stack
        @return: the value of top time
        """
        if self.size == 0:
            return None
        item_to_remove = self.top_item
        self.top_item = item_to_remove.get_link_node()
        self.size -= 1
        return item_to_remove.get_value()

    def push(self, value):
        """
        Pushes a value to the top of stack
        If the space is full, this method will do nothing
        @param value: value to be pushed
        """
        if not self._has_space():
            return
        new_node = Node(value)
        new_node.set_link_node(self.top_item)
        self.top_item = new_node
        self.size += 1

    def reset_from_list(self, value_list: list):
        """
        Builds or **reset** stack from list of values
        The first value in the list will be the value of top item and the last value in the list will be pushed first
        This method should **not** make changes to the input list
        This method will do nothing if the size of input list is larger than the limit of stack
        @param value_list: list is values
        """
        self.top_item = None  # reset the whole stack
        self.size = 0  # reset size
        copy_list = value_list.copy()
        while copy_list:
            self.push(copy_list.pop(-1))

    def to_list(self):
        """
        Traverse the stack from the top item the bottom item to a list from beginning from the top item
        @return: <list> list representing the stack
        """
        result_list = []
        current = self.top_item
        while current is not None:
            result_list.insert(len(result_list), current.get_value())
            current = current.get_link_node()
        return result_list
