from cs50 import get_int

def main():
    # Loop continuously until the user gives a valid height
    while True:
        height = get_int("Height: ")
        if 1 <= height <= 8:
            break

    # Generate the right-aligned pyramid row by row
    for row in range(1, height + 1):
        spaces = height - row
        hashes = row
        print(" " * spaces + "#" * hashes)

if __name__ == "__main__":
    main()
