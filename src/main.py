from hvlcs import highest_value_lcs

# Main program
def main():
    # Get the input file path from the user
    file_path = input("Enter the input file path: ")

    characters = {}

    # Try to open the file at the file path
    try:
        with open(file_path, 'r') as f:
            # Get number of characters K
            K = int(f.readline().strip())

            # Get each character and its corresponding value in each line
            for i in range(K):
                char, val = f.readline().split()
                characters[char] = int(val)

            A = f.readline().strip()
            B = f.readline().strip()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Validate K
    if K < 1:
        print("Error: K = 0.")
        return
    
    # Validate number of characters
    if len(characters) != K:
        print("Error: Number of characters != K.")
        return
    
    # Check that A only contains characters from our dict
    if not set(A).issubset(characters):
        print("Error: String A contains something outside our characters dict.")
        return
    
    # Check that B only contains characters from our dict
    if not set(B).issubset(characters):
        print("Error: String B contains something outside our characters dict.")
        return
    
    # Call our dynamic algorithm
    final_val, subsequence = highest_value_lcs(A, B, characters)

    # Print the max value and corresponding subsequence
    print(f"Maximum Value of Subsequence: {final_val}")
    print(f"Subsequence: {subsequence}")

    # Write the hits/misses into an output file
    o_file_path = input("Enter the output file path: ")

    # Write to output file
    try:
        with open(o_file_path, 'w') as f:
            f.write(str(final_val) + "\n")
            f.write(subsequence)
        print("Wrote output to file.")
    except FileNotFoundError:
        print("Output file not found, exiting.")
                

if __name__ == "__main__":
    main()
