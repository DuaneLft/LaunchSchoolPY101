#Rock Paper Scissors 2
import random
import os
import platform
VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
VALID_CHOICES_2 = ['r', 'p', 'sc', 'sp', 'l']
TRANSLATOR = {
    'r': 'rock', 'p': 'paper', 'sc': 'scissors', 'l': 'lizard', 'sp': 'spock',
}
WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper','spock'],
    'spock': ['rock', 'scissors'],
}
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def input_format(player):
    if player in VALID_CHOICES_2:
        return TRANSLATOR[player]
    return player
def prompt(message):
    print(f'==>{message}')

def score_tally(player, computer):
    prompt(f"The score is player: {player[0]}, computer: {computer[0]}\n")
    if player[0] == 3:
        clear_screen()
        prompt("You Win!")
    elif computer[0] == 3:
        clear_screen()
        prompt("Computer Wins!")
    else:
        prompt("Next round")

def compute_winner(player, computer, player_total, computer_total):
    if player == computer:
        prompt(f"It's a tie\n player {player} computer {computer}")
    elif computer in WINNING_COMBOS[player]:
        player_total[0] += 1
        prompt(f"You won that round.\nplayer {player} computer {computer}")
    else:
        computer_total[0] += 1
        prompt(f"""Computer won that round.
            Player {player}
            Computer {computer}""")

def play_game():
    player_score = [0]
    computer_score = [0]
    prompt("""   Welcome to Rock Paper Scissors Lizard Spock.
            This is a variation of the classic rock, paper, scissor game.
            In this game Rock beats Scissors and Lizard. 
            Paper beats Rock and Spock.
            Scissors beats Paper and Lizard. 
            Lizard beats Paper and Spock.
            Spock beats Rock and Scissors.\n
            You can use the following abbreviations while playing this game.
            r for rock,
            p for paper,
            sc for scissors,
            l for lizard,
            sp for spock.\n
            Or you can spell out each choice.
            The first one to 3 wins is the Champion!\n""")

    while True:
        prompt(f"Choose one: {', '.join(VALID_CHOICES)}\n")
        player_choice = input().lower().strip()
        player_choice = input_format(player_choice)
        while (
            (player_choice not in VALID_CHOICES) and
            (player_choice not in VALID_CHOICES_2)
        ):
            prompt('That is not a valid choice.')
            player_choice = input().lower().strip()
            player_choice = input_format(player_choice)
        computer_choice = random.choice(VALID_CHOICES)
        compute_winner(
            player_choice,
            computer_choice,
            player_score,
            computer_score
            )
        score_tally(player_score, computer_score)

        while True:
            answer = 'yes'
            if (player_score[0] == 3) or (computer_score[0] == 3):
                player_score[0] = 0
                computer_score[0] = 0
                prompt("Do you want to play again? (y/n).")
                answer = input().lower()
                if answer.startswith('n') or answer.startswith('y'):
                    break
                prompt("That's not a valid choice.")
            else:
                break
        if answer[0] == 'n':
            break

play_game()