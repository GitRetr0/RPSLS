import random
import tkinter as tk
from tkinter import messagebox
def play_rock_paper_scissors(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    result = f"Computer chose: {computer_choice}\n"
    if user_choice == computer_choice:
            result += "Both players selected {user_choice}. It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
):
        result += "You win!"
    else:
        result += "You lose!"
    
    messagebox.showinfo(computer_choice, result)
        
def create_interface():
    root = tk.Tk()
    root.title("Rock-Paper-Scissors")
    tk.Label(root, text="Choose your move: ", font=("Arial", 14)).pack(pady=10)
    for choice in ["rock", "paper", "scissors"]:
        tk.Button(root, text=choice.capitalize(), font=("Arial", 12), command=lambda c=choice: play_rock_paper_scissors(c)).pack(pady=5)
    root.mainloop()
    
if __name__=="__main__":
    create_interface()