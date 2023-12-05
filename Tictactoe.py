from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        if check_winner():
            label.config(text=f"{player} wins")
            highlight_winner_cells(row, column)
        elif not empty_spaces():
            label.config(text="Tie!")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} turn")

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    return False

def empty_spaces():
    return sum(row.count('') for row in buttons) == 0

def highlight_winner_cells(row, column):
    for i in range(3):
        buttons[row][i].config(bg="green")
        buttons[i][column].config(bg="green")

    if row == column:
        buttons[i][i].config(bg="green")

    if row + column == 2:
        buttons[i][2 - i].config(bg="green")

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)

buttons = [['' for _ in range(3)] for _ in range(3)]

label = Label(text=f"{player} turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda r=row, c=column: next_turn(r, c))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
