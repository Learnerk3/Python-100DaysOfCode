# from distutils.command.clean import clean
import random
import hangManArt
import hangManWords
import os

print(hangManArt.logo)
letters_list = list(random.choice(hangManWords.word_list))
print(''.join(letters_list))

dash_list = ["_" for length in range(len(letters_list))]
# print(' '.join(dash_list))
is_gameOver = False
count = 1
while not is_gameOver:
    user_guess = input("Guess a letter: ")
    os.system('cls')
    if user_guess in dash_list:
        print(f"You've already guessed {user_guess}")
    if user_guess in letters_list:
        for i in range(len(letters_list)):
            if user_guess == letters_list[i]:
                dash_list[i] = user_guess
        print(' '.join(dash_list))
        if dash_list == letters_list:
            print("You win.")
            is_gameOver = True          
    else:
            print(' '.join(dash_list))
            print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
            if count == 6:
                print("You lose.")
                is_gameOver = True
            count += 1
    print(hangManArt.stages[len(hangManArt.stages) - (count)])
    


# count = 0 
# print(hangManArt.logo)
# letters_list = list(random.choice(hangManWords.word_list))
# print(''.join(letters_list))
# user_guess = input("Guess a letter: ")
# # print(letters_list)
# dash_list = ["_" for num in range(len(letters_list))]
# # while count < 5:
# life = len(hangManArt.stages) - 1
# for letter in letters_list:
#     if user_guess == letter:
#         dash_list[letters_list.index(letter)] = letter
#     #     dash_list[letters_list.index(letter)] = user_guess
#     #     os.system('cls')
#     #     print(' '.join(dash_list))
#     #     print(hangManArt.stages[-1])
#     #     user_guess = input("Guess a letter: ")
#     # else:
#     #     os.system('cls')
#     #     print(' '.join(dash_list))
#     #     print(f"You guessed {user_guess}, that's not in the word. You lose a life")
#     #     print("You lose.")
#     #     print(hangManArt.stages[life - 1])
#     #     user_guess = input("Guess a letter: ")
# # if user_guess in letters_list:
# #     letter_index = letters_list.index(user_guess)
# #     dash_list[letter_index] = user_guess
    
# # else:
#     # os.system('cls')
#     # print(hangManArt.stages[len(hangManArt.stages)-1])
