def count_file_contents(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        word_count += len(line.split())
        char_count += len(line)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")

# Example usage
filename = 'sample.txt'  # Make sure this file exists in the same folder
count_file_contents(filename)
