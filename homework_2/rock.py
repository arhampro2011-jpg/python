import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissor"]

def rock():
    play_game("Rock")

def paper():
    play_game("Paper")

def scissor():
    play_game("Scissor")

def play_game(player_choice):
    program_choice = random.choice(choices)

    player_label.config(text="You: " + player_choice)
    program_label.config(text="Program: " + program_choice)

    if player_choice == program_choice:
        result_label.config(text="It's a Tie!")
    elif (player_choice == "Rock" and program_choice == "Scissor") or \
         (player_choice == "Paper" and program_choice == "Rock") or \
         (player_choice == "Scissor" and program_choice == "Paper"):
        result_label.config(text="You Win!")
    else:
        result_label.config(text="Program Wins!")

def reset_game():
    player_label.config(text="You: -")
    program_label.config(text="Program: -")
    result_label.config(text="Make your choice!")

window = tk.Tk()
window.title("Rock Paper Scissor")
window.geometry("500x400")
window.resizable(False, False)

title = tk.Label(window, text="Rock Paper Scissor", font=("Arial", 25, "bold"))
title.pack(pady=25)

instruction = tk.Label(window, text="Choose your move", font=("Arial", 14))
instruction.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

rock_button = tk.Button(
    button_frame,
    text="Rock",
    font=("Arial", 13),
    width=10,
    command=rock
)
rock_button.grid(row=0, column=0, padx=8)

paper_button = tk.Button(
    button_frame,
    text="Paper",
    font=("Arial", 13),
    width=10,
    command=paper
)
paper_button.grid(row=0, column=1, padx=8)

scissor_button = tk.Button(
    button_frame,
    text="Scissor",
    font=("Arial", 13),
    width=10,
    command=scissor
)
scissor_button.grid(row=0, column=2, padx=8)

player_label = tk.Label(window, text="You: -", font=("Arial", 15))
player_label.pack(pady=10)

program_label = tk.Label(window, text="Program: -", font=("Arial", 15))
program_label.pack(pady=5)

result_label = tk.Label(
    window,
    text="Make your choice!",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)

reset_button = tk.Button(
    window,
    text="Reset Game",
    font=("Arial", 12),
    width=15,
    command=reset_game
)
reset_button.pack(pady=10)

window.mainloop()