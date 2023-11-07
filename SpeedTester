import random
import time

def generate_random_text():
    text = "The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs."
    return ' '.join(random.choice(text.split()) for _ in range(30))

def calculate_typing_speed(input_text, elapsed_time):
    words = input_text.split()
    num_words = len(words)
    wpm = (num_words / elapsed_time) * 60
    return wpm

def main():
    print("Welcome to the Typing Speed Tester!")
    input("Press Enter to start...")

    random_text = generate_random_text()
    print("Type the following text:")
    print(random_text)

    start_time = time.time()

    user_input = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    user_wpm = calculate_typing_speed(user_input, elapsed_time)

    print(f"You typed at {user_wpm:.2f} words per minute (WPM).")
    print("Good job!")

if __name__ == "__main__":
    main()
