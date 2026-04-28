class FileHandler:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = []

    def read_file(self):
        try:
            with open(self.input_file, 'r') as file:
                self.data = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found.")
        except Exception as e:
            print(f"Error: {e}")
