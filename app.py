import random

words = ["python", "apple", "banana", "computer", "school"]


word = random.choice(words)


guessed_word = ["_"] * len(word)


guessed_letters = []

attempts = 6

print("Welcome to Hangman!")
print("Guess the word letter by letter.")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", attempts)

    guess = input("Enter a letter: ").lower()


    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

   
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
