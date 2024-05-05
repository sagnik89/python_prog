"""
This is the game of blackjack.

Rules: 
At first, the player is assigned the card and displayed

Also the first card of computer is displayed.

The user gets the choice of pulling another card or betting right away

the question is asked to the user until the user decides to bet

then the bet is shown and the winner is declared. 

the closest number to 21 after addition of the value of the cards of both the players wins the game

the king, queen and the jack is awarded 10 points and other cards the value of their respective card

For setting the algorithm of the computer picking cards:
    keep taking on cards until u r at a difference of 5 with 21. if the difference between the sum of your 
    cards and 21 exceed 5 stop taking cards 


"""

logo = """
.------.            _     _            _    _            _                                   
|A_  _ |.          | |   | |          | |  (_)          | |                                                  
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __                                              
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


import random
import os
from clear import clear

emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}

def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

def last_display(userH, compH, userT, compT):
    print(f'Your final hand: {userH}, final score: {userT}')
    print(f'Computer\'s hand: {compH}, final score: {compT}')



user_hand = []
comp_hand = []

user_won = False

# For the computer hand 

comp_total = 0
while abs(21 - comp_total) > 5:
    rand = random.randint(1, 10)
    comp_hand.append(rand)
    comp_total = sum_list(comp_hand)

# For the user hand 
user_hand = [random.randint(1, 10), random.randint(1, 10)]
user_total = sum_list(user_hand)

should_continue = True


while should_continue:

    print(logo)

    continuity = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no ")

    
    # For the computer hand 

    comp_hand = []
    comp_total = 0
    while abs(21 - comp_total) > 5:
        rand = random.randint(1, 10)
        comp_hand.append(rand)
        comp_total = sum_list(comp_hand)

    # For the user hand 
    user_hand = [random.randint(1, 10), random.randint(1, 10)]
    user_total = sum_list(user_hand)



    if continuity == 'y':
        should_continue = True
    else:
        should_continue = False
        exit()

    print(f'Your cards: {user_hand}, current score: {user_total}')
    print(f'Computer\'s first card: {comp_hand[0]}')
    
    if continuity != 'n':
        cardDrawn = True
    
    while cardDrawn:



        card_draw = input("Type 'y' to get another card, type 'n' to pass ")

        if card_draw == 'y':

            user_hand.append(random.randint(1, 10))
            user_total = sum_list(user_hand)

            cardDrawn = True
            print(f'Your cards: {user_hand}, current score: {user_total}')
            print(f'Computer\'s first card: {comp_hand[0]}')
            if user_total > 21:
               last_display(userT=user_total, userH=user_hand, compH=comp_hand, compT=comp_total)
               print(f"You went over! You lose the game {emoji_dict['crying']}")
               cardDrawn = False
               
        else:
            cardDrawn = False
        
    
    if ((abs(21 - comp_total) > abs(21 - user_total)) or comp_total > 21) and user_total <= 21:
        last_display(userT=user_total, userH=user_hand, compH=comp_hand, compT=comp_total)
        print(f"You won the game {emoji_dict['happy']}")
    elif user_total <= 21:
        last_display(userT=user_total, userH=user_hand, compH=comp_hand, compT=comp_total)    
        print(f"You lose the game {emoji_dict['crying']}")
    else:
        continuity = 'n'

        s = input("Press Enter to proceed: ")

        os.system("clear")
        continue
    
    continuity = 'n'

    s = input("Press Enter to proceed: ")

    os.system("clear")

    
    
    
    

# Also i don't think this is the moist optimised code. Have to work on optimising it
# have to fix the issue when both have the same score
# Also fix the issue when both the person get higher score than 21

