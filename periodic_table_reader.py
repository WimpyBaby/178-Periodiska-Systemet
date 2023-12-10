"""A program that reads a periodic table file and creates a periodic table."""

from element import Element


class PeriodicTableReader:
    """A class for reading a periodic table file."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.element_dict = self._create_element_dict()

    def _create_element_dict(self):
        # Create an empty dictionary
        element_dict = {}
        # Open the file and read it
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split()

                # Check if data is not empty and create an element object
                if data:
                    symbol, weight, number, row, column = data
                    element = Element(
                        symbol, float(weight), int(number), int(row), int(column)
                    )
                    # Add the element instances to the dictionary
                    element_dict[symbol] = element
        return element_dict

    def show_element(self):
        """function for showing elements in a dictionary"""
        print(
            "\nSymbol         Weight          Number          Row             Column\n"
        )
        # Loop through the dictionary and print the values
        for symbol, element in self.element_dict.items():
            print(
                f"{symbol:<15} {element.weight:<15} {element.number:<15} {element.row:<15} {element.column:<15}"
            )
