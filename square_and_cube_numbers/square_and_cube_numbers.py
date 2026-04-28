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