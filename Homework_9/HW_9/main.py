from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from tic_tac_toe import show_matrix, cheking, player_1, player_2
from calc_bot import calc, convert_num
from phone_num import write_number, show_number

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("player1", player_1)) # Игра "Крестики-нолики" для первого игрока
app.add_handler(CommandHandler("player2", player_2)) # Игра "Крестики-нолики" для второго игрока
app.add_handler(CommandHandler("calc", calc)) # Решение примеров типа, 12+5, 4/2
app.add_handler(CommandHandler("writenum", write_number)) # Запись новых номеров в файл csv
app.add_handler(CommandHandler("shownums", show_number)) # Показывает все номера, сохраненные файле csv

print('start')

app.run_polling()