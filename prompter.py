import time

def display_highlighted_text(text, words_per_minute):
    """Display the text chunk, highlighting words as they should be read."""
    words = text.split()
    interval = 60 / words_per_minute  # seconds per word

    sentence_endings = {".", "!", "?"}  # Characters that indicate end of a sentence

    for i, word in enumerate(words):
        # Calculate the start and end indices for the window
        start_idx = max(0, i - 10)
        end_idx = min(len(words), i + 11)

        # Highlight the current word in the chunk
        window_words = words[start_idx:i] + [f"\033[1;31m{word}\033[0m"] + words[i+1:end_idx]
        highlighted = " ".join(window_words)

        # Print the highlighted text without clearing the screen
        print(f"\033c{highlighted}", end="", flush=True)

        # Wait before proceeding to the next word
        time.sleep(interval)

        # Check for end of sentence and pause briefly
        if word[-1] in sentence_endings or (i + 1 < len(words) and words[i + 1][0].isupper()):
            time.sleep(0.5)  # Pause after each sentence

    # Ensure the full text is shown at the end
    print("\033c" + " ".join(words))

if __name__ == "__main__":
    print("Welcome to the Teleprompter!")
    
    # Ask for the text to be displayed
    text = input("Enter the chunk of text to be used:\n")

    # Validate and ask for words-per-minute
    while True:
        try:
            wpm = int(input("Enter the words-per-minute (WPM) rate: "))
            if wpm <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer for WPM.")

    print("\nPress Enter when ready to start...")
    input()

    # Display the highlighted text
    display_highlighted_text(text, wpm)
