# Rock Paper Scissor Game
import random
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
computer_score = 0
player_score = 0
replay = True
def score_tally(player, computer):
    prompt(f"The score is player: {player}, computer: {computer}\n")
    if player == 5:
        prompt("You Win!")
    elif computer == 5:
        prompt("Computer Wins!")
    else:
        prompt("Next round")
def prompt(message):
    print(f'==>{message}')
def display_winner(player, computer):
    if ((player == "rock" and computer == "scissors") or
        (player == "rock" and computer == "lizard") or
        (player == "paper" and computer == "spock") or
        (player == "paper" and computer == "rock") or
        (player == "lizard" and computer == "paper") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "rock") or
        (player == "spock" and computer == "scissors") or
        (player == "scissors" and computer == "lizard") or
        (player == "scissors" and computer == "paper")):
        prompt("You win this game!")
        global player_score
        player_score += 1
    elif (((player == "rock") and ((computer == "paper") or (computer == "spock"))) or
        ((player == "spock") and ((computer == "paper") or (computer == "lizard"))) or
        ((player == "lizard") and ((computer == "rock") or (computer == "scissors"))) or
        ((player == "paper") and ((computer == "scissors") or (computer == "lizard"))) or
        ((player == "scissors") and ((computer == "rock") or (computer == "spock")))):
        prompt("Computerr wins this game!")
        global computer_score
        computer_score += 1
    else:
        prompt("It's a tie!")

while True:
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input()
    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice!')
        choice = input()
    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {choice}, computer chose {computer_choice}')
    display_winner(choice,computer_choice)
    replay = score_tally(player_score, computer_score)
    while True:
        if (player_score == 5) or (computer_score == 5):
            player_score = 0
            computer_score = 0
            prompt("Do you want to play again (y/n)")
            answer = input().lower()
            if answer.startswith('n') or answer.startswith('y'):
                break
            else:
                prompt("That's not a valid choice")
        else:
            answer = "yes"
            break

    if answer[0] == 'n':
        break
    
  

