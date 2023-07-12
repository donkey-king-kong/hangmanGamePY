from random_word import RandomWords
import time

hangman = {
1:'''
  +---+
      |
      |
      |
      |
      |
=========''',
2:'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
3:'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
4:'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
5:'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
6:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
7:'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
8:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
9:'''
  +---+
  |   |
  O   |
      |
 /|\  |
 / \  |
=========''',
}

print("Welcome to HangMan Game!")
print("------------------------", end="\n")
word = RandomWords().get_random_word()
guess = []
for _ in range(len(word)):
    guess += "_"
count = 0

while "_" in guess:
    print("------------------------")
    print("Word: ", end="")
    print("".join(guess))
    print(f"Its a {len(word)} letter word.")
    char = input("\nGuess the letter: ").lower()
    for _ in range(len(word)):
        if word[_] == char:
            guess[_] = char
    print("\n")
    if char not in word:
        print("Guess again!")
        count += 1
        print(hangman[count])
        time.sleep(0.7)
        if count == 9:
            print(f"Game Over! Nice try. The word was {word}")
            quit()
    else:
        print("Nice!")
    print("\n")
    time.sleep(0.5)
    print("\n\n\n")
print("You win! The word was: " + word)
