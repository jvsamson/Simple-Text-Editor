"""
Created on Tue Apr 11 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""

class PositionalList:
    """A positional list is a container of elements that keeps track of the position of each element.

    This module provides the PositionalList class that represents a doubly-linked list with sentinel
    header and trailer nodes. The PositionalList can be used for various applications that require
    efficient manipulation of elements at different positions.
    """

    class _Node:
        """A node of a doubly-linked list with a reference to an element, previous node, and next node."""

        def __init__(self, element, prev=None, nxt=None):
            self._element = element
            self._prev = prev
            self._nxt = nxt

    def __init__(self):
        self._header = self._Node(None)
        self._trailer = self._Node(None)
        self._header._nxt = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def _insert_between(self, e, predecessor, successor):
        """Insert an element between two nodes and return the new node."""
        new = self._Node(e, predecessor, successor)
        predecessor._nxt = new
        successor._prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        """Delete a node and return its element."""
        predecessor = node._prev
        successor = node._nxt
        predecessor._nxt = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._nxt = node._element = None
        return element

    def insert_after(self, p, e):
        """Insert an element e after position p."""
        if p._nxt is None:
            return self._insert_between(e, p, self._trailer)
        else:
            return self._insert_between(e, p, p._nxt)

    def delete(self, p):
        """Delete the element at position p."""
        return self._delete_node(p)

    def first(self):
        """Return the first node."""
        return self._header._nxt

    def last(self):
        """Return the last node."""
        return self._trailer._prev

    def after(self, p):
        """Return the node after the node at position p."""
        return p._nxt

    def is_end(self, p):
        """Return True if the position p is at the end, else return False."""
        return p._nxt == self._trailer

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def __iter__(self):
        """Iterate over the elements in the list."""
        cursor = self.first()
        while cursor != self._trailer:
            yield cursor._element
            cursor = cursor._nxt

    def __str__(self):
        """Return the string representation of the list."""
        return ''.join(list(self))
    
    def _getNodeAtPosition(self, pos):
        """Return the node at the given position."""
        if pos < 0 or pos > self._size:
            raise ValueError("Invalid position")
        
        current_node = self._header
        for _ in range(pos + 1):
            current_node = current_node._nxt
        return current_node
