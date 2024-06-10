import random
import hangman_stages
import word_file

# word_list = ["apple", "beautiful", "potato", ]
lives = 6

chosen_word = random.choice(word_file.words)
# print(chosen_word)

display=[]
for letter in range(len(chosen_word)):
    display += '_'


print("Let's Play Hangman!!")
print("You have only 6 lives so try to guess the word within 6 attempts! Good luck !!")
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives = lives-1
        print("You guessed", guessed_letter, "that is not present in the word. So you lose a life")
        print(lives, "lives remaining.")
        print(display)
        if lives == 0:
            game_over = True
            print("You lose!!")
            print("The correct answer was", chosen_word)
    if '_' not in display:
        game_over = True
        print("You won!!!")
    print(hangman_stages.stages[lives])
