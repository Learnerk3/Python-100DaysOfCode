#Step 2

from dis import dis
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')



display = ["_" for i in range(len(chosen_word))]
is_gameOver = False
while not is_gameOver:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
          print("You lose.")
          is_gameOver = True
    print(f"{' '.join(display)}")
    word = ''.join(display)
    if chosen_word == word:
        is_gameOver = True
        print("You win.")
    print(stages[lives])