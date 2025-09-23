from art import *
from info import data
import random

"""Format the data from info"""
def format_data(item):
    item_name = item['name']
    item_description = item['description']
    item_country = item['country']
    return f"{item_name}, a {item_description}, from {item_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'

    else:
        return user_guess == 'b'

#Display art
print(logo)
score = 0
gameover = False
item_b = random.choice(data)
#Geerate a random account from the information
while gameover == False:

# Making item at position B become in position A

    item_a = item_b
    item_b = random.choice(data)

    if item_a == item_b:
        item_b = random.choice(data)

    print(f"Compare A: {format_data(item_a)}")
    print(vs)
    print(f"Compare B: {format_data(item_b)}")

    #Ask the user for a guess
    guess = input("Who has more followers? 'A' or 'B'?\n").lower()

    #Check if the user is correct
    ## Get follower count of each account and use if statement to chek if user is correct
    a_follower_count = item_a['follower_count']
    b_follower_count = item_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    #Give the user feedback
    if is_correct:
        score += 1
        print(f"Your right! Current score is {score}")
    else:
        print(f"Sorry, that's wrong. Game over. Final score is {score}")
        gameover = True

#Make game repeatable

#Make position B go to A after guess

