"""A module for creating a periodic table GUI."""

import tkinter as tk
from tkinter import scrolledtext
import random


class PeriodicTableGUI:
    """A class for creating a periodic table GUI."""

    def __init__(self, root, element_dict):
        self.root = root
        self.element_dict = element_dict
        self.question_label = None
        self.generated_symbol = None
        self.correct_answer = []
        self.wrong_answer = []
        self.buttons = {}
        self.chances = 3
        self.attempts = 0
        self.text_area = scrolledtext.ScrolledText(
            self.root, width=80, height=20, wrap=tk.WORD
        )
        self.text_area.pack()

        self.show_elements()

    def create_periodic_table(self):
        """Create a periodic table."""

        while True:
            # Generate a random symbol
            self.generated_symbol = random.choice(list(self.element_dict))

            if self.generated_symbol not in self.correct_answer:
                break

        # Clear the window with previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.attempts = 0

        # create a label for the question
        self.question_label = tk.Label(
            self.root,
            text=f"Where in the table is : {self.generated_symbol} located?",
        )
        self.question_label.grid(row=0, column=0, columnspan=18)

        for symbol, element in self.element_dict.items():
            # Create a button for each element
            button = tk.Button(
                self.root,
                text=element.number,
                borderwidth=1,
                relief="solid",
                width=5,
                height=2,
            )
            button.grid(row=element.row, column=element.column, padx=5, pady=5)
            button.config(
                command=lambda btn=button, num=element.number: self.button_row_col(
                    btn, num
                )
            )
            self.buttons[symbol] = button

    def button_row_col(self, button, num):
        """Get the row and column of the button."""

        # Check if the button is the correct answer
        if self.element_dict[self.generated_symbol].number == num:
            self.correct_answer.append(button)
            correct_label = tk.Label(self.root, text="Correct!")
            correct_label.grid(row=2, column=0, columnspan=18)

            self.create_periodic_table()

        # If the button is not the correct answer
        else:
            self.attempts += 1
            self.wrong_answer.append(button)
            button.config(bg="red")  # Change button color to red

            wrong_label = tk.Label(self.root, text="Wrong!")
            wrong_label.grid(row=2, column=0, columnspan=18)

            chances_label = tk.Label(
                self.root, text=f"You have {self.chances-self.attempts} left"
            )
            chances_label.grid(row=1, column=0, columnspan=18)

            # if the user has used all the chances
            if self.attempts == self.chances:
                self.disable_buttons()
                answer_label = tk.Label(
                    self.root,
                    text=f"Sorry, the correct answer is {self.element_dict[self.generated_symbol].number}",
                )
                answer_label.grid(row=2, column=0, columnspan=18)

                # Create a try again button
                try_again_button = tk.Button(
                    self.root,
                    text="Try again?",
                    command=lambda: self.create_periodic_table(),
                )
                try_again_button.grid(row=3, column=0, columnspan=18)

                # Create an exit button
                exit_button = tk.Button(
                    self.root, text="Exit", command=lambda: self.close_window()
                )
                exit_button.grid(row=3, column=0, columnspan=16)

    def clear_wrong_answer(self):
        """Clear the wrong answer list."""
        for button in self.wrong_answer:
            button.config(bg="SystemButtonFace")

    def disable_buttons(self):
        """Disable all buttons."""
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)

    def close_window(self):
        """Close the window."""
        self.root.destroy()

    def show_elements(self):
        """function for showing elements in a dictionary"""
        self.text_area.delete(1.0, tk.END)
        header = (
            "\nSymbol         Weight          Number          Row             Column\n"
        )
        self.text_area.insert(tk.INSERT, header)

        for symbol, element in self.element_dict.items():
            row_data = f"{symbol:<15}{element.weight:<15}{element.number:<15}{element.row:<15}{element.column:<15}\n"
            self.text_area.insert(tk.INSERT, row_data)

    def run_show_elements(self):
        """Run the show_elements function."""
        self.show_elements()
