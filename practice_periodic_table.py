"""A class for practicing periodic table."""

import random
import error_handling as eh


class PracticePeriodicTable:
    """A class for practicing periodic table."""

    def __init__(self, element_dict):
        self.element_dict = element_dict

    def practice_element_number(self):
        """Practice periodic system numbers."""

        attempt = 3
        total_attempt = 0

        # Generate a random symbol
        generated_symbol = random.choice(list(self.element_dict.keys()))
        generated_number = self.element_dict[generated_symbol].number

        # Debugging print statements
        print(
            f"\n{generated_symbol} {self.element_dict[generated_symbol].weight} {generated_number}"
        )

        while True:
            # Ask user for input
            guess = eh.get_number_input(
                f"\nWhich atomic number does {generated_symbol} have? "
            )

            # Check if guess is equal to generated_number
            if int(guess) == self.element_dict[generated_symbol].number:
                print("Correct!")
                break

            total_attempt += 1
            print(f"Wrong! you have {attempt - total_attempt} attempts left")

            if total_attempt == 3:
                print(
                    f"\nSorry, the correct answer is {self.element_dict[generated_symbol].number}"
                )
                break

    def practice_element_symbol(self):
        """Practice periodic system symbols."""

        # Set attempt and total_attempt to 0
        attempt = 3
        total_attempt = 0

        # Generate a random symbol and element from element_dict
        generated_symbol = random.choice(list(self.element_dict))
        generated_element = self.element_dict[generated_symbol]

        # Debugging print statements
        print(
            f"\n{generated_symbol} {generated_element.weight} {generated_element.number}"
        )

        while True:
            # Ask user for input
            guess = eh.get_letters_input(
                f"\nWhich symbol does {generated_element.number} have? "
            )
            # Check if guess is equal to generated_symbol
            if guess.casefold() == generated_symbol.casefold():
                print("Correct!")
                break

            # If guess is not equal to generated_symbol
            total_attempt += 1
            print(f"Wrong! You have {attempt - total_attempt} attempts left")

            # If total_attempt is equal to 3
            if total_attempt == 3:
                print(f"\nSorry, the correct answer is {generated_symbol}")
                break

    def practice_element_weight(self):
        """Practice periodic system weights."""
        # Extracting a random element from element_dict as the correct weight
        generated_symbol = random.choice(list(self.element_dict))
        generated_weight = self.element_dict[generated_symbol].weight

        # Extracting random elements from element_dict as alternatives
        random_symbols = random.sample(list(self.element_dict), 2)
        random_weights = [
            self.element_dict[symbol].weight for symbol in random_symbols
        ] + [generated_weight]

        # Shuffling the order of the weights
        random.shuffle(random_weights)

        # Debugging print statements
        print(
            f"Generated symbol: {generated_symbol} {self.element_dict[generated_symbol].weight}\n"
        )

        # Printing the shuffled weights
        print(
            f"What is the correct weight for {generated_symbol}?: \n{random_weights}\n"
        )

        # Asking the user to input their choice
        while True:
            user_choice = eh.get_float_input(
                ("Which weight do you think is correct? Enter the weight: ")
            )

            if user_choice in random_weights:
                if user_choice == generated_weight:
                    print("\nCorrect!\n")
                    break
                print(f"\nWrong! The correct answer is {generated_weight}\n")
                break
            print("\nInvalid input! Please enter a valid alternative.\n")
