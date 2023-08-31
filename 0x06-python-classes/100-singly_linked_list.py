#!/usr/bin/python3
"""Linked list definition"""


class Node:
    """This class reps a Node"""
    def __init__(self, data, next_node=None):
        """
        Inits a new Node object.

        Args:
            data (int): The data in the neu node.
            next_node (Node): The next linked node. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """returns(int) the data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data stored in the node.

        Args:
            value(int): New node value.

        Raises:
            TypeError: If value != int.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns(Node) the next node in the list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the list.

        Args:
            value(Node): Neu next node.

        Raises:
            TypeError: If value != Node/None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class reps a singly-linked list"""

    def __init__(self):
        """Inits a new SinglyLinkedList object(PIA)"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts neu Node into the sorted pst in the list(increase).

        Args:
            value(int): The value to insert.
        """
        neu_node = Node(value)

        if self.__head is None:
            self.__head = neu_node
            neu_node.next_node = None
        elif value < self.__head.data:
            neu_node.next_node = self.__head
            self.__head = neu_node
        else:
            bucket = self.__head
            while (bucket.next_node is not None and
                    bucket.next_node.data < value):
                bucket = bucket.next_node
            neu_node.next_node = bucket.next_node
            bucket.next_node = neu_node

    def __str__(self):
        """Returns a string rep of the linked list(str)"""
        res = ""
        bucket = self.__head
        while bucket is not None:
            res += str(bucket.data) + "\n"
            bucket = bucket.next_node
        return res.rstrip("\n")
