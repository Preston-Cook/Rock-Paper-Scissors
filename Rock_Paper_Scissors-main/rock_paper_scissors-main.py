from random import choice
from time import sleep
import pygame
pygame.mixer.init()

def spacer():
    print('-'*40)

pygame.mixer.music.load('Assets/theme.wav')
pygame.mixer.music.play(-1)

NAVIGATION = pygame.mixer.Sound('Assets/navigation.wav')
WIN = pygame.mixer.Sound('Assets/correct_guess.wav')
LOSS = pygame.mixer.Sound('Assets/wrong_guess.wav')
WIN_GAME = pygame.mixer.Sound('Assets/win.wav')
LOSE_GAME = pygame.mixer.Sound('Assets/lose.wav')

move_dic = {
    'ROCK' : """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    
    'PAPER' : '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''',
    'SCISSORS' : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
}

possible_moves = list(move_dic)

while True:
    computer_score = 0
    user_score = 0
    spacer()
    print('ROCK, PAPER, SCISSORS'.center(40,'-'))
    spacer()
    print('''
To Play: Enter 1

To Quit: Enter 2
''')
    print('-'*40+'\n')
    user_selection = input('Enter a Selection: ')
    NAVIGATION.play()
    while user_selection not in ['1','2']:
        print('ERROR: Invalid Input')
        user_selection = input('Enter a Selection: ')
        NAVIGATION.play()
    if user_selection == '2':
        print()
        spacer()
        print('QUITTING PROGRAM'.center(40,'-'))
        spacer()
        quit()
    else:
        print()
        spacer()
        print('TIME TO PLAY!'.center(40,'-'))
        spacer()
        while user_score < 5 and computer_score < 5:
            computer_move = choice(possible_moves)
            user_move = input('\nEnter a move: ').upper()
            NAVIGATION.play()
            while user_move not in possible_moves:
                print('ERROR: Invalid Input')
                user_move = input('Enter a move: ').upper()
                NAVIGATION.play()
            sleep(1)
            spacer()
            print(f'YOU CHOSE {user_move}'.center(40,'-'))
            spacer()
            print(move_dic[user_move])
            spacer()
            print(f'THE COMPUTER CHOSE {computer_move}'.center(40,'-'))
            spacer()
            print(move_dic[computer_move])
            spacer()
            if (user_move == 'ROCK' and computer_move == 'SCISSORS') or (user_move == 'PAPER' and computer_move == 'ROCK') or (user_move == 'SCISSORS' and computer_move == 'PAPER'):
                print('YOU WIN THE ROUND!'.center(40,'-'))
                WIN.play()
                user_score += 1
            elif user_move != computer_move:
                print('YOU LOSE THE ROUND!'.center(40,'-'))
                LOSS.play()
                computer_score += 1
            else:
                print("THERE WAS A TIE!".center(40,'-'))
            spacer()
            print(f"CURRENT SCORE: USER {user_score} COMPUTER {computer_score}".center(40))
            spacer()
        if user_score == 5:
            print('YOU WIN THE GAME!'.center(40))
            WIN_GAME.play()
        else:
            print('YOU LOSE THE GAME!'.center(40))
            LOSE_GAME.play()
