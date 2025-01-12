import re
import argparse

def read_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        file_data = f.readlines()
    
    for line in file_data:
        if not line.startswith('>') and not line.startswith('//'):
            data.append(line.strip())
    return ''.join(data)

def find_longest_repeated_subsequence(sequence):
    substrings = {}
    for i in range(0, len(sequence)):
        for j in range(0, len(sequence)):
            if i == j:
                continue
            substring = sequence[i:j]
            substrings[substring] = sequence.count(substring)

    # find all duplicates
    duplicates = [k for k,v in substrings.items() if v > 1]
    longest_dup = max(duplicates, key=len)  # find longest
    return longest_dup


def calculate_gc_content(sequence):
    g_count = sequence.lower().count('g')
    c_count = sequence.lower().count('c')
    total_count = g_count + c_count
    return (total_count / len(sequence)) * 100

def main():
    parser = argparse.ArgumentParser(description="Analyze genetic sequences.")
    parser.add_argument("file", help="Path to file.")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated subsequence.")
    parser.add_argument("--gc", action="store_true", help="Calculate GC content.")

    arg_parser = parser.parse_args()

    sequence = read_file(arg_parser.file)

    if arg_parser.duplicate:
        longest_repeated = find_longest_repeated_subsequence(sequence)
        print(f"Longest repeated subsequence: {longest_repeated}")

    if arg_parser.gc:
        gc_content = calculate_gc_content(sequence)
        print(f"GC content: {round(gc_content, 2)}%")


if __name__ == "__main__":
    main()