"""
Created on Tue Apr 11 23:25:12 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
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
    print("3: Insert characters just after the cursor")
    print("4: Delete the character just after the cursor")
    print("5: Exit the editor")
    print("")

editor = TextEditor()

print_instructions()

while True:
    command = input("Enter a command: ")

    if command == "1":
        editor.move_left()
    elif command == "2":
        editor.move_right()
    elif command == "3":
        while True:
            input_characters = input('Input a character or "\\" for a new command: ')
            if input_characters == "\\":
                break
            elif len(input_characters) == 1:
                editor.insert(input_characters)
                print(editor)
                print("")
            else:
                print("Invalid input. Please provide one character, a whitespace or '\\' to exit insertion mode.")
    elif command == "4":
        editor.delete()
    elif command == "5":
        break
    elif command == '99':
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
