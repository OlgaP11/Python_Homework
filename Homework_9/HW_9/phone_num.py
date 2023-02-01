from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import csv

async def write_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.split()
    del text[0]
    with open ('phone_base.csv', mode='a',encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = ',', lineterminator = '\r')
        file_writer.writerow(text)
    await update.message.reply_text ('Данные успешно внесены.')

async def show_number (update: Update, context: ContextTypes.DEFAULT_TYPE):
    book = ''
    with open ('phone_base.csv', mode='r',encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter = ",")
        for row in file_reader:
            book = book + str(row) +'\n'
        book = book.replace('[','')
        book = book.replace(']','')
        book = book.replace("'",'')
    await update.message.reply_text(f'{book}')
            

