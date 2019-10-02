"""
Linked List class
"""
from interview.utils.node import Node


class LinkedList:

    def __init__(self, value=None, ref_list='', by_list=False):
        """
        Can be constructed in two ways, when by_list is true, it constructs with ref_list otherwise it constructs with
        value
        @param value: value of head node
        @param ref_list: reference list for reconstructing the linked list
        @param by_list: <bool> whether we use reference list to construct
        """
        self._head_node = Node(value=value)
        if by_list is True:
            self._construct_from_list(ref_list)

    def _construct_from_list(self, ref_list):
        """
        **Reconstructs** the linked list from a list of values
        @param ref_list: reference list for constructing the linked list
        """
        self._head_node = Node(ref_list[0])
        [self.add_value_to_the_end(item) for item in ref_list[1:]]

    def add_value_to_the_end(self, value):
        """
        @param value: value to be added
        Add the value to the end of linked list
        """
        new_node = Node(value)
        if not self._head_node:
            self._head_node = new_node
            return
        current = self._head_node
        while current.get_link_node():
            current = current.get_link_node()
        current.set_link_node(new_node)

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

    def remove_first_node_by_value(self, value):
        """
        Removes node by its **value**
        This will remove the first nodes by the value
        With Python, node will be removed automatically by garbage collection if no reference was pointing to it
        @param value: value of node(s) we want to remove
        """
        if self._head_node.get_value() == value:
            self._head_node = self._head_node.get_link_node()
            return
        current = self._head_node
        next_node = current.get_link_node()
        while next_node:
            if next_node.get_value() == value:
                current.set_link_node(next_node.get_link_node())
                return
            current = current.get_link_node()
            next_node = current.get_link_node() if current is not None else None

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

#
# def run():
#     n2 = Node('value2')
#     n3 = Node('value3')
#     l = LinkedList('value1')
#     l._head_node.set_link_node(n2)
#     n2.set_link_node(n3)
#     print(l.stringify_list())
#     v1 = 'value'
#     l.add_value_to_the_end(v1)
#     print(l.stringify_list())
#
#
# if __name__ == "__main__":
#     run()
