def write_multiple_lines(filename='mylife.txt'):
    with open(filename, 'w') as file:
        while True:
            line = input("Enter line: ")
            file.write(line + "\n")

            choice = input("Are there more lines y/n? ").lower()
            if choice != 'y':
                break

    print(f"All lines successfully saved to {filename}")

write_multiple_lines()