class NumberProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = self._read_numbers()

    def _read_numbers(self):
        try:
            with open(self.input_file, 'r') as file:
                return [int(num) for num in file.read().split()]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
            return []

    def process(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def write_to_file(self, output_file, data):
        with open(output_file, 'w') as file:
            for num in data:
                file.write(str(num) + "\n")

class EvenProcessor(NumberProcessor):
    def process(self):
        even_squared = [num**2 for num in self.numbers if num % 2 == 0]
        self.write_to_file("double.txt", even_squared)
        print("Even numbers squared written to double.txt")

class OddProcessor(NumberProcessor):
    def process(self):
        odd_cubed = [num**3 for num in self.numbers if num % 2 != 0]
        self.write_to_file("triple.txt", odd_cubed)
        print("Odd numbers cubed written to triple.txt")