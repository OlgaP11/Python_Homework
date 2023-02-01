from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def convert_num(msg,symbol):
    n1 = msg[5:msg.rfind(symbol)]
    n2 = msg[msg.rfind(symbol)+1:]
    if 'i' in msg:
        msg = msg.replace('i','j')
        if 'j' in n1:
            n1 = complex(n1)
            n2 = float(n2)
        elif 'j' in n2:
            n2 = complex(n2)
            n1 = float(n1)
    else:
        n1, n2 = float(n1), float(n2)
    return n1, n2

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if '+' in text:
        num1, num2 =convert_num(text,'+')
        await update.message.reply_text (f'{num1} + {num2} = {round(num1+num2,2)}')
    elif '-' in text:
        num1, num2 =convert_num(text,'-')
        await update.message.reply_text (f'{num1} - {num2} = {round(num1-num2,2)}')
    elif '*' in text:
        num1, num2 =convert_num(text,'*')
        await update.message.reply_text (f'{num1} * {num2} = {round(num1*num2,2)}')
    elif '/' in text:
        num1, num2 =convert_num(text,'/')
        await update.message.reply_text (f'{num1} / {num2} = {round(num1/num2,2)}')