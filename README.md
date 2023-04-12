# Text Editor with Positional List
Extra Credit Assignment 1 -Data Structures &amp; Algorithms S-2023 - Hertie School

This project is a simple text editor that uses a doubly-linked list with sentinel header and trailer nodes to store and display a string of characters. The text editor allows users to perform various operations like moving the cursor left/right, inserting a character, and deleting a character.

### The code consists of three files:

1. positional_list.py: Contains the PositionalList class, which is a container of elements that keeps track of the position of each element. The PositionalList class represents a doubly-linked list with sentinel header and trailer nodes. The class provides methods for inserting elements, deleting elements, navigating the list, and more.
2. text_editor.py: Contains the TextEditor class, which uses the PositionalList class to store and display a string of characters along with a cursor object that highlights a position in the string. The TextEditor class provides methods for moving the cursor left/right, inserting a character, and deleting a character.
3. interface.py: This module acts as an interface for the TextEditor. It provides a user-friendly command-line interface to interact with the TextEditor by creating an editor instance, performing operations like inserting characters, moving the cursor, and deleting characters, and then displaying the resulting text.

### How to Use:

1. Move the cursor left: Type '1' and press Enter.
2. Move the cursor right: Type '2' and press Enter.
3. Insert a character 'c' just after the cursor: Type '3 c' and press Enter (replace 'c' with the character you want to insert).
4. Delete the character just after the cursor: Type '4' and press Enter.
5. Exit the editor: Type '5' and press Enter.

### Important Notes:
* For the 'insert' command, use the format '3 x', where x is the character you want to insert.
* The cursor is represented by the '|' symbol in the text editor.
