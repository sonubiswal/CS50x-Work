import csv
import sys

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.file_exit(1) if hasattr(sys, 'file_exit') else sys.exit(1)

    # Read database file into a list of dictionaries
    database = []
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            database.append(row)
        # Extract the STR sequences from the header column (excluding 'name')
        str_sequences = reader.fieldnames[1:]

    # Read DNA sequence text file into a string
    with open(sys.argv[2]) as f:
        dna_sequence = f.read()

    # Find longest match of each STR in DNA sequence
    run_counts = {}
    for str_seq in str_sequences:
        run_counts[str_seq] = longest_match(dna_sequence, str_seq)

    # Check database for matching profiles
    for person in database:
        match = True
        for str_seq in str_sequences:
            if int(person[str_seq]) != run_counts[str_seq]:
                match = False
                break
        if match:
            print(person["name"])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
