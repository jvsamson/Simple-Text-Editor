"""
Created on Tue Apr 11 21:25:12 2023

@author: j.v.samson
"""

from text_editor import TextEditor


"""
This module acts as an interface for the TextEditor.

It provides a user-friendly command-line interface to interact with the TextEditor by
creating an editor instance, performing operations like inserting characters, moving the cursor,
and deleting characters, and then displaying the resulting text.
"""

def print_instructions():
    print(" Text Editor Commands:")
    print("1: Move the cursor left")
    print("2: Move the cursor right")
    print("3 [c]: Insert a character 'c' just after the cursor")
    print("4: Delete the character just after the cursor")
    print("5: Exit the editor")
    print("Note: For the 'insert' command, use the format '3 x', where x is the character you want to insert.")
    print("")


editor = TextEditor()

print_instructions()

while True:
    user_input = input("Enter a command: ").strip().lower()
    command_parts = user_input.split()

    if len(command_parts) == 0:
        print("Invalid command. Please try again.")
        continue

    command = command_parts[0]

    if command == "1":
        editor.move_left()
    elif command == "2":
        editor.move_right()
    elif command == "3":
        if len(command_parts) == 2:
            editor.insert(command_parts[1])
        else:
            print("Invalid format for the 'insert' command. Use the format 'insert x', where x is the character you want to insert.")
    elif command == "4":
        editor.delete()
    elif command == "5":
        break
    elif command_parts[0] == '99':
            print("")
            print("Maintenance:")
            cursor_position = editor.get_cursor_position()
            node = editor._text._getNodeAtPosition(cursor_position)
            print(f'Before insertion - Cursor position: {cursor_position} List: ')
            print(f'Node at position {cursor_position} : {node}')
            print("")
            print(f'List length: {len(editor._text)}')
            print("List structure:")
            for i, elem in enumerate(editor._text):
                node = editor._text._getNodeAtPosition(i)
                print(f'Node at position {i}: {node} (prev: {node._prev}, next: {node._nxt})')

    else:
        print("Invalid command. Please try again.")

    print(editor)
    print("")

print("Thank you for using the Text Editor!")
print("")
