# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:50:32 2021

@author: JENI
"""

import random

def play():
    user = input("Enter your desired choice:'r' for Rock, 'p' for Paper, and 's' for Scissors \n")
    computer = random.choice(['r', 'p','s'])
    
    
    if user  == computer:
        return 'Its a tie!'
    elif user != 'r' or 'p' or 's':
        print('Please enter an option , r or p or s.')
        play()
        
        
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You lost!'
        
def is_win(player, opponent):
    # This function would return true if player wins, but there are conditions.
    # r > s, s > p, p > r
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' \
        or player == 'p' and opponent == 'r':
            return 'You won!'
        

print(play())