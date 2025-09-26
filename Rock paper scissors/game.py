import random
# ASCII Art for Rock, Paper, Scissors
ascii_art = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "paper": '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}
def rock_paper_scissors():
    gameover = False
    while gameover == False:
        user_choice = input("Rock, paper, or scissors:\n").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])


        print(user_choice)
        print(ascii_art.get(user_choice))
        print(computer_choice)
        print(ascii_art.get(computer_choice))

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors()