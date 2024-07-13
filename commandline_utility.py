import argparse

def count_file_stats(input_file):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(input_file, 'r') as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += len(line)

    return line_count, word_count, char_count

def main():
    parser = argparse.ArgumentParser(description='File Statistics Utility')
    parser.add_argument('input_file', help='Input file path')

    args = parser.parse_args()
    input_file = args.input_file

    line_count, word_count, char_count = count_file_stats(input_file)

    print(f"File statistics for {input_file}:")
    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of characters: {char_count}")

if __name__ == '__main__':
    main()
