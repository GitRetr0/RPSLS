import random
import tkinter as tk
from tkinter import messagebox
def play_rock_paper_scissors(user_choice):
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    computer_choice = random.choice(choices)
    
    result = f"Computer chose: {computer_choice}\n"
    if user_choice == computer_choice:
            result += f"Both players selected {user_choice}. It's a tie!"
    else:
        #winning conditions
        winning_moves = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }
    if computer_choice in winning_moves[user_choice]:
        result += f"{user_choice} beats {computer_choice}. You win!"
    else:
        result += f"{computer_choice} beats {user_choice} You lose!"
    
    messagebox.showinfo(computer_choice, result)
        
def create_interface():
    game_name = "Rock, Paper. Scissors, Lizard. Spock"
    root = tk.Tk()
    root.title(game_name)
    tk.Label(root, text="Choose your move: ", font=("Arial", 14)).pack(pady=10)
    for choice in ["rock", "paper", "scissors", "lizard", "spock"]:
        tk.Button(root, text=choice.capitalize(), font=("Arial", 12), command=lambda c=choice: play_rock_paper_scissors(c)).pack(pady=5)
    root.mainloop()
    
if __name__=="__main__":
    create_interface()