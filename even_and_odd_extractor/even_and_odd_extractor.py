class FileHandler:
    def __init__(self, input_file):
        self.input_file = input_file
        self.numbers = []

    def read_numbers(self):
        try:
            with open(self.input_file, 'r') as file:
                self.numbers = [int(line.strip()) for line in file]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
        except ValueError:
            print("Error: File contains non-integer values.")

    def write_numbers(self, output_file, data):
        with open(output_file, 'w') as file:
            for num in data:
                file.write(f"{num}\n")