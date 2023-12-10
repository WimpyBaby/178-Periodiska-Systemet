"""Code for practicing periodic system numbers, weight and symbol."""


import sys
import tkinter as tk
import error_handling as eh
from periodic_table_reader import PeriodicTableReader
from practice_periodic_table import PracticePeriodicTable
from periodic_table_gui import PeriodicTableGUI


# ELEMENTS_DATA = eh.get_file_input("What is the name for your file? ")
ELEMENTS_DATA = "element.txt"
reader = PeriodicTableReader(ELEMENTS_DATA)
practice_table_instance = PracticePeriodicTable(reader.element_dict)


def displaymenu():
    """Menu for periodic system."""
    print("\n---------------MENU---------------")
    print("Welcome to the periodic system!\n")
    print("1. Show elements")
    print("2. Practice element number")
    print("3. Practice element Symbol")
    print("4. Practice element weight")
    print("5. Practice periodic table")
    print("6. Exit")
    print("----------------------------------")
    user_input = eh.get_number_input("Please enter your choice: ")

    if user_input == "1":
        root = tk.Tk()
        periodic_table_gui_instance = PeriodicTableGUI(root, reader.element_dict)
        root.title("Elements in the periodic table")
        periodic_table_gui_instance.show_elements()
    elif user_input == "2":
        practice_table_instance.practice_element_number()
    elif user_input == "3":
        practice_table_instance.practice_element_symbol()
    elif user_input == "4":
        practice_table_instance.practice_element_weight()
    elif user_input == "5":
        root = tk.Tk()
        periodic_table_gui_instance = PeriodicTableGUI(root, reader.element_dict)
        root.title("Periodic Table")
        periodic_table_gui_instance.create_periodic_table()
        root.mainloop()
    elif user_input == "6":
        sys.exit()
    else:
        print("Invalid input! Please enter a number between 1-5.")


def main():
    """Main function to run the periodic system."""

    while True:
        displaymenu()


# Main program starts here with instance of PeriodicTableReader
if __name__ == "__main__":
    main()
