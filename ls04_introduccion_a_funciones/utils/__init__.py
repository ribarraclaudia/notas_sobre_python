from os import system
import platform

def clear_screen():
    """Clean the console.
    """
    if platform.system() == 'Windows':
        _ = system('cls')
    else:
        _ = system('clear')

def system_pause():
    """Display a message and wait enter key.
    """
    _ = input('\nPress Enter key to continue . . . ')