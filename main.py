import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")
current_player = "X"
buttons = []

def check_winner():
    filled_cells = 0
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] != "":
                filled_cells += 1

    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            return True
        if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            return True
        if filled_cells == 9:  # Проверка на ничью
            messagebox.showinfo("Игра окончена", "Ничья!")
            return None  # Возвращаем None для обозначения ничьей

    return False


def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] !="":
        return
    buttons[row][col]["text"]=current_player

     #Проверка на победу
    if check_winner() is True:
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
    elif check_winner() is None:
        return  # Ничья, ничего не делаем

    current_player = "O" if current_player == "X" else "X"             # переключение игроков

#внешн цикл
for i in range(3):            #Здесь i — это номер текущей строки
    row = []
    for j in range(3):       # второй цикл
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))

        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)
window.mainloop()