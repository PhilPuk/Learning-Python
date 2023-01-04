import random

def get_winner(player1_choice, player2_choice):
  if player1_choice == player2_choice:
    return "tie"
  if player1_choice == "rock":
    if player2_choice == "paper":
      return "player2"
    else:
      return "player1"
  if player1_choice == "paper":
    if player2_choice == "scissors":
      return "player2"
    else:
      return "player1"
  if player1_choice == "scissors":
    if player2_choice == "rock":
      return "player2"
    else:
      return "player1"

def play_computer_game():
  player_choice = input("Enter rock, paper, or scissors: ")
  computer_choice = random.choice(['rock', 'paper', 'scissors'])
  print(f"Player choice: {player_choice}")
  print(f"Computer choice: {computer_choice}")
  winner = get_winner(player_choice, computer_choice)
  if winner == "tie":
    print("Tie!")
  elif winner == "computer":
    print("Computer wins!")
  else:
    print("Player wins!")

def play_player_game():
  player1_choice = input("Player 1, enter rock, paper, or scissors: ")
  player2_choice = input("Player 2, enter rock, paper, or scissors: ")
  print(f"Player 1 choice: {player1_choice}")
  print(f"Player 2 choice: {player2_choice}")
  winner = get_winner(player1_choice, player2_choice)
  if winner == "tie":
    print("Tie!")
  elif winner == "player1":
    print("Player 1 wins!")
  else:
    print("Player 2 wins!")

mode = input("Enter '1' for player vs computer or '2' for player vs player: ")
if mode == '1':
  play_computer_game()
elif mode == '2':
  play_player_game()
else:
  print("Invalid input. Please try again.")
