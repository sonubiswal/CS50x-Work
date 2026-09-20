from cs50 import get_string

def main():
    # Get string input from the user
    text = get_string("Text: ")

    letters = 0
    words = 1  # Start at 1 because spaces separate words
    sentences = 0

    # Count letters, words, and sentences
    for char in text:
        if char.isalpha():
            letters += 1
        elif char == " ":
            words += 1
        elif char in [".", "!", "?"]:
            sentences += 1

    # Calculate Coleman-Liau index variables
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Corrected Coleman-Liau formula with 0.296 * S
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Output the reading grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()
