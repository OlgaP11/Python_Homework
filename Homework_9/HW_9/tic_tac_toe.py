from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint

def show_matrix (matrix):
    curr_field = ''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            curr_field = curr_field + str(matrix[i][j]) + ' '
        curr_field += '\n'
    return curr_field

field = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]    
count = 9

def cheking ():
    global count
    if field[0][0] == field[0][1] == field[0][2] or\
        field[1][0] == field[1][1] == field[1][2] or\
        field[2][0] == field[2][1] == field[2][2] or\
        field[0][0] == field[0][1] == field[0][2] or\
        field[0][1] == field[1][1] == field[2][1] or\
        field[2][0] == field[2][1] == field[2][2] or\
        field[0][0] == field[1][1] == field[2][2] or\
        field[0][2] == field[1][1] == field[0][2]:
        count = 0
    else:
        count -= 1
    return count
    
async def player_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Напишите номер, выбранной клетки: ')
    index = update.message.text.split()
    for i in range(len(field)):
        for j in range(len(field)):
            if int(index[1]) == field[i][j]:
                field[i][j] = 'X'
                break
    curr_count = cheking()
    if curr_count == 0:
        await update.message.reply_text(f'Победил игрок 1.')
    else: 
        await update.message.reply_text(f'Количество доступных ходов {count}')
    await update.message.reply_text(f'{show_matrix(field)}')

async def player_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Напишите номер, выбранной клетки: ')
    index = update.message.text.split()
    for i in range(len(field)):
        for j in range(len(field)):
            if int(index[1]) == field[i][j]:
                field[i][j] = '0'
                break
    curr_count = cheking()
    if curr_count == 0:
        await update.message.reply_text(f'Победил игрок 2.')
    else: 
        await update.message.reply_text(f'Количество доступных ходов {count}')
    await update.message.reply_text(f'{show_matrix(field)}')
