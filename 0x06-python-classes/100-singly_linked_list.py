#!/usr/bin/python3
"""
Class Node that defines a node of a singly linked list by:

- Private instance attribute: data:
  * property def data(self): to retrieve it
  * property setter def data(self, value): to set it:
    . data must be an integer, otherwise raise a TypeError exception with the
      message data must be an integer

- Private instance attribute: next_node:
  * property def next_node(self): to retrieve it
  * property setter def next_node(self, value): to set it:
    . next_node can be None or must be a Node, otherwise raise a TypeError
      exception with the message next_node must be a Node object

- Instantiation with data and next_node: def __init__(self, data,
  next_node=None)
"""


class Node:
    """ The class Node define a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """ The __init__ method use.

        Args:
        - data (int): the data of the node
        - next_node (Node): the next_node  of the node, and can be None

        Attribute:
        - __data
        - __next_node
        """
        self.__data = data
        self.__next_node = next_node

        if type(data) != int:
            raise TypeError('data must be an integer')

        elif type(next_node) != Node and next_node is not None:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """
        @property data method retrieve the data
        Return the data of a node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        @data.setter method change the data of a node

        Args:
        - value (int): the value of a node
        """
        self.__data = value

        if type(value) != int:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """
        @property next_node method retrieve the next node
        Return the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        @next_node.sette method set the next node

        Args:
        - value (Node): the node and must be None
        """
        self.__next_node = value

        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """ The class SinglyLinkedList define the head."""

    def __init__(self):
        """ The __init__ method use.

        Args:
        - head (None): the head of a node
        """
        self.__head = None

    def sorted_insert(self, value):
        """ The sorted_insert inserts a new Node into the correct sorted
        position in the list (increasing order).

        Args:
        - value (int): the position to insert sorted node
        """

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __repr__(self):
        """The repr method indicate how to print the linked list"""

        sll = []
        tmp = self.__head
        while (tmp is not None):
            sll.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(sll)
