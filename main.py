
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики до 3 побед")
window.geometry("300x450")  # Увеличили окно для счётчика

current_player = "X"
buttons = []
scores = {"X": 0, "0": 0}  # Счётчик побед

# Виджеты для отображения счёта
score_label = tk.Label(window, text="Счёт: X - 0 | 0 - 0", font=("Arial", 12))
score_label.grid(row=4, column=0, columnspan=3, pady=10)

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def reset_board():
    for row in buttons:
        for btn in row:
            btn.config(text="")

def update_score():
    score_label.config(text=f"Счёт: X - {scores['X']} | 0 - {scores['0']}")

def check_game_over():
    if scores["X"] >= 3:
        messagebox.showinfo("Игра окончена", "Игрок X победил в матче!")
        reset_game(full_reset=True)
    elif scores["0"] >= 3:
        messagebox.showinfo("Игра окончена", "Игрок 0 победил в матче!")
        reset_game(full_reset=True)

def reset_game(full_reset=False):
    global current_player
    current_player = "X"
    reset_board()
    if full_reset:
        scores["X"] = 0
        scores["0"] = 0
    update_score()

def on_click(row, col):
    global current_player

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        scores[current_player] += 1
        update_score()
        messagebox.showinfo("Победа!", f"Игрок {current_player} выиграл раунд!")
        reset_board()
        check_game_over()
        return

    if all(btn['text'] != "" for row in buttons for btn in row):
        messagebox.showinfo("Ничья!", "Раунд окончен вничью!")
        reset_board()
        return

    current_player = "0" if current_player == "X" else "X"

# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                       command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопки управления
reset_btn = tk.Button(window, text="Новая игра", font=("Arial", 12),
                     command=lambda: reset_game(full_reset=True))
reset_btn.grid(row=5, column=0, columnspan=3, pady=5, sticky="ew")

window.mainloop()
