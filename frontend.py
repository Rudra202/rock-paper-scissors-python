import tkinter as tk
from tkinter import messagebox
from backend import RockPaperScissorsGame


class GameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("520x450")
        self.root.resizable(False, False)
        self.root.config(bg="grey")

        self.game = RockPaperScissorsGame()

        self.title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 20, "bold"),
            bg="grey",
            fg="white"
        )
        self.title_label.pack(pady=15)

        self.info_label = tk.Label(
            self.root,
            text="First to 5 points wins!",
            font=("Arial", 12),
            bg="grey",
            fg="white"
        )
        self.info_label.pack(pady=5)

        self.score_label = tk.Label(
            self.root,
            text="Player: 0    Computer: 0",
            font=("Arial", 14, "bold"),
            bg="grey",
            fg="blue"
        )
        self.score_label.pack(pady=10)

        self.player_choice_label = tk.Label(
            self.root,
            text="Your Choice: ",
            font=("Arial", 13),
            bg="grey",
            fg="white"
        )
        self.player_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(
            self.root,
            text="Computer Choice: ",
            font=("Arial", 13),
            bg="grey",
            fg="white"
        )
        self.computer_choice_label.pack(pady=5)

        self.result_label = tk.Label(
            self.root,
            text="Result: ",
            font=("Arial", 14, "bold"),
            bg="grey",
            fg="yellow"
        )
        self.result_label.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg="grey")
        self.button_frame.pack(pady=20)

        self.rock_button = tk.Button(
            self.button_frame,
            text="Rock",
            font=("Arial", 12, "bold"),
            width=12,
            bg="black",
            fg="red",
            activebackground="black",
            activeforeground="red",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.play_round("Rock")
        )
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(
            self.button_frame,
            text="Paper",
            font=("Arial", 12, "bold"),
            width=12,
            bg="black",
            fg="red",
            activebackground="black",
            activeforeground="red",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.play_round("Paper")
        )
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(
            self.button_frame,
            text="Scissors",
            font=("Arial", 12, "bold"),
            width=12,
            bg="black",
            fg="red",
            activebackground="black",
            activeforeground="red",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.play_round("Scissors")
        )
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 12, "bold"),
            width=15,
            bg="black",
            fg="red",
            activebackground="black",
            activeforeground="red",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=self.reset_game
        )
        self.reset_button.pack(pady=15)

    def play_round(self, player_choice):
        if self.game.check_game_winner() is not None:
            return

        computer_choice = self.game.computer_choice()
        winner = self.game.decide_winner(player_choice, computer_choice)

        self.player_choice_label.config(text=f"Your Choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer Choice: {computer_choice}")

        if winner == "Tie":
            self.result_label.config(text="Result: It's a Tie!", fg="orange")
        elif winner == "Player":
            self.result_label.config(text="Result: You Win This Round!", fg="lightgreen")
        else:
            self.result_label.config(text="Result: Computer Wins This Round!", fg="#ff6666")

        self.score_label.config(
            text=f"Player: {self.game.player_score}    Computer: {self.game.computer_score}"
        )

        game_winner = self.game.check_game_winner()
        if game_winner:
            if game_winner == "Player":
                messagebox.showinfo("Game Over", "Congratulations! You reached 5 points and won the game!")
            else:
                messagebox.showinfo("Game Over", "Computer reached 5 points and won the game!")
        else:
            self.root.after(1500, self.reset_round_message)

    def reset_round_message(self):
        self.result_label.config(text="Result: Choose again", fg="yellow")

    def reset_game(self):
        self.game.reset_game()
        self.score_label.config(text="Player: 0    Computer: 0")
        self.player_choice_label.config(text="Your Choice: ")
        self.computer_choice_label.config(text="Computer Choice: ")
        self.result_label.config(text="Result: ", fg="yellow")


if __name__ == "__main__":
    root = tk.Tk()
    app = GameUI(root)
    root.mainloop()