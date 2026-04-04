import time
import matplotlib.pyplot as plt

from hvlcs import highest_value_lcs

def main():
    
    files = []
    for i in range(0, 10):
        files.append("../tests/empirical/" + str(i+1) + ".in")
    sizes = []

    # List to record runtimes.
    listRunTime = []

    # Test each .in file and see how string length scales runtime
    for fileName in files:
        characters = {}

        # Try to open the file at the file path
        try:
            with open(fileName, 'r') as f:
                # Get number of characters K
                K = int(f.readline().strip())

                # Get each character and its corresponding value in each line
                for i in range(K):
                    char, val = f.readline().split()
                    characters[char] = int(val)

                A = f.readline().strip()
                B = f.readline().strip()

                sizes.append(len(A))
        except FileNotFoundError:
            print(f"Error: The file {fileName} was not found.")
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

        # Start and stop timer for running highest_value_lcs() with specific input.
        start = time.time()
        final_val, subsequence = highest_value_lcs(A, B, characters)
        end = time.time()

        print(f"{fileName}: {final_val}, {subsequence}")

        # Calculate running time and store in listRunTime.
        runtime = end - start
        listRunTime.append(runtime)

    # Plot line graph of gale_shapley() runtimes.
    plt.subplot(1, 2, 1)
    plt.plot(sizes, listRunTime, color='blue', marker='o')
    plt.grid(True)
    plt.title("Runtimes of highest_value_lcs()")
    plt.xlabel("Input size (n == m)")
    plt.ylabel("Runtime")

    plt.suptitle("Runtimes for Highest Value Longest Common Subsequence")
    plt.show()

if __name__ == "__main__":
    main()