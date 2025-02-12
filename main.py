import tkinter as tk
from tkinter import messagebox
import random

# Функция для генерации случайного цвета
def random_color(exclude_colors=[]):
    while True:
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if color not in exclude_colors:
            return color

def setup_game():
    global window_color, color_x, color_o
    # Генерируем случайный цвет для окна
    window_color = random_color()
    window.configure(bg=window_color)

    # Определяем цвета для X и O
    color_x = random_color([window_color])
    color_o = random_color([window_color, color_x])

def choose_symbol():
    global current_player
    choice_window = tk.Toplevel(window)
    choice_window.title("Выбор символа")

    tk.Label(choice_window, text="Выберите, чем будете играть:").pack(pady=10)

    def set_symbol(symbol):
        global current_player, player_symbol
        current_player = symbol
        player_symbol = symbol  # Сохраняем выбранный символ
        choice_window.destroy()  # Закрываем окно выбора
        setup_game()  # Настраиваем игру после выбора символа
        create_buttons()  # Создание кнопок после выбора символа

    tk.Button(choice_window, text="Крестик (X)", command=lambda: set_symbol("X")).pack(pady=5)
    tk.Button(choice_window, text="Нолик (O)", command=lambda: set_symbol("O")).pack(pady=5)

# Создаем основное окно
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

# Выбор символа перед началом игры
choose_symbol()

buttons = []
game_over = False  # Переменная для отслеживания состояния игры

player1_wins = 0
player2_wins = 0
player_symbol = None  # Переменная для хранения выбранного символа игрока

def create_buttons():
    global buttons
    buttons = []  # Сброс кнопок перед созданием нового игрового поля
    for i in range(3):
        row = []
        for j in range(3):
            btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                            command=lambda r=i, c=j: on_click(r, c), bg=window_color)
            btn.grid(row=i, column=j)
            row.append(btn)
        buttons.append(row)

def check_winner():
    global player1_wins, player2_wins, game_over

    for i in range(3):
        # Проверка горизонталей
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            if buttons[i][0]["text"] == "X":
                player1_wins += 1
            else:
                player2_wins += 1
            game_over = True  # Игра окончена
            return True

        # Проверка вертикалей
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            if buttons[0][i]["text"] == "X":
                player1_wins += 1
            else:
                player2_wins += 1
            game_over = True
            return True

    # Проверка диагоналей
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        if buttons[0][0]["text"] == "X":
            player1_wins += 1
        else:
            player2_wins += 1
        game_over = True
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        if buttons[0][2]["text"] == "X":
            player1_wins += 1
        else:
            player2_wins += 1
        game_over = True
        return True

    # Проверка на ничью
    filled_cells = sum(button["text"] != "" for row in buttons for button in row)
    if filled_cells == 9:
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()  # Перезапускаем игру при ничьей
        return None

    return False

def reset_game():
    global current_player, game_over
    game_over = False  # Сбрасываем состояние игры
    setup_game()  # Обновляем цвета для новой игры
    for row in buttons:
        for button in row:
            button["text"] = ""
            button["bg"] = window_color  # Сбрасываем цвет кнопок на цвет окна

    current_player = player_symbol  # Сохраняем выбор символа игрока

def on_click(row, col):
    global current_player
    if game_over or buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player
    # Устанавливаем цвет кнопки в зависимости от игрока
    if current_player == "X":
        buttons[row][col]["bg"] = color_x
    else:
        buttons[row][col]["bg"] = color_o

    if check_winner() is True:
        if player1_wins == 3:  
            messagebox.showinfo("Победитель!", "Игрок 1 одержал 3 победы!")
            window.destroy()  # Закрываем окно после 3 побед
        elif player2_wins == 3:
            messagebox.showinfo("Победитель!", "Игрок 2 одержал 3 победы!")
            window.destroy()  # Закрываем окно после 3 побед
        else:
            messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
            reset_game()  # Сброс игры после победы
    elif check_winner() is None:
        return  # Ничья

    current_player = "O" if current_player == "X" else "X"  # Переключение игроков

# Запуск основного цикла приложения
window.mainloop()


