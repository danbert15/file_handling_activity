def write_multiple_lines(filename="mylife.txt"):
    with open(filename, 'w') as file:
        while True:
            line = input("Enter line: ")
            file.write(line + "\n")