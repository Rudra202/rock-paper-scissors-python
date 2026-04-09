#------ game logic -----#

import random


class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.winner_score = 5

    def computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, player, computer):
        if player == computer:
            return "Tie"

        if (
            (player == "Rock" and computer == "Scissors")
            or (player == "Paper" and computer == "Rock")
            or (player == "Scissors" and computer == "Paper")
        ):
            self.player_score += 1
            return "Player"

        self.computer_score += 1
        return "Computer"

    def check_game_winner(self):
        if self.player_score >= self.winner_score:
            return "Player"
        elif self.computer_score >= self.winner_score:
            return "Computer"
        return None

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0