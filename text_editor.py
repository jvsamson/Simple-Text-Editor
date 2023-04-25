"""
Created on Tue Apr 11 2023

@author: j.v.samson
"""

from positional_list import PositionalList

class TextEditor:
    """A text editor that uses a positional list to store and display a string of characters.

    This module provides the TextEditor class, which uses a PositionalList to store and display
    a string of characters along with a cursor object that highlights a position in the string.
    The editor supports operations like moving the cursor left/right, inserting a character, and deleting
    a character.
    """

    def __init__(self):
        self._text = PositionalList()
        self._cursor_pos = 0

    def move_left(self):
        if self._cursor_pos == 0:
            print("The cursor is already at the beginning of the list.")
        else:
            self._cursor_pos -= 1

    def move_right(self):
        if self._cursor_pos == len(self._text):
            print("The cursor is already at the end of the list.")
        else:
            self._cursor_pos += 1

    def insert(self, character):
        if self._cursor_pos == 0:
            node = self._text._header
        else:
            node = self._text._getNodeAtPosition(self._cursor_pos - 1)
        #new_node = self._text._insert_between(character, node, node._nxt)
        self._cursor_pos += 1

    def delete(self):
        """Delete the character just after the cursor."""
        if self._cursor_pos < len(self._text):
            self._text.delete(self._text._getNodeAtPosition(self._cursor_pos))

    def __str__(self):
        """Return the string representation of the text in the editor."""
        cursor_display = '|'
        text_display = ''.join(str(e) for e in self._text)
        return text_display[:self._cursor_pos] + cursor_display + text_display[self._cursor_pos:]
    
    def get_cursor_position(self):
        """Return the cursor position."""
        return self._cursor_pos
