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

class StudentProcessor(FileHandler):
    def __init__(self, input_file):
        super().__init__(input_file)
        self.students = []

    def parse_data(self):
        for line in self.data:
            try:
                name, gwa = line.split(',')
                self.students.append((name.strip(), float(gwa.strip())))
            except ValueError:
                print(f"Skipping invalid line: {line}")

    def get_highest_gwa(self):
        if not self.students:
            return None
        # In GWA system, LOWER value = BETTER (1.0 is highest)
        return min(self.students, key=lambda x: x[1])

    def process(self):
        self.read_file()
        self.parse_data()

        top_student = self.get_highest_gwa()

        if top_student:
            name, gwa = top_student
            print("Top Student:")
            print(f"Name: {name}")
            print(f"GWA: {gwa}")
        else:
            print("No valid student data found.")

