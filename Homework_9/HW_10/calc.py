from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import log_in as log

def multi(task):
    task.insert(task.index('*')-1, task[task.index('*')-1] * task[task.index('*')+1])
    del task[task.index('*')-1]
    del task[task.index('*')+1]
    del task[task.index('*')]
    return task

def div(task):
    task.insert(task.index('/')-1, task[task.index('/')-1] / task[task.index('/')+1])
    del task[task.index('/')-1]
    del task[task.index('/')+1]
    del task[task.index('/')]
    return task

def plus(task):
    task.insert(task.index('+')-1, task[task.index('+')-1] + task[task.index('+')+1])
    del task[task.index('+')-1]
    del task[task.index('+')+1]
    del task[task.index('+')]
    return task

def minus(task):
    task.insert(task.index('-')-1, task[task.index('-')-1] - task[task.index('-')+1])
    del task[task.index('-')-1]
    del task[task.index('-')+1]
    del task[task.index('-')]
    return task

async def main(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = update.message.text
    text = text.replace('/calc ','')
    log('user_task', text)

    # Добавление пробелов рядом со знаками и создание списка
    if '*' in text:
        text = text.replace('*',' * ')
    if '/' in text:
        text = text.replace('/',' / ')
    if '+' in text:
        text = text.replace('+',' + ')
    if '-' in text:
        text = text.replace('-',' - ')
    if '(' in text:
        text = text.replace('(', ' ( ')
    if ')' in text:
        text = text.replace(')', ' ) ')
    text = text.split()

    # Перевод чисел в другой формат
    for i in range(len(text)):
        if text[i].isdigit():
            text[i] = float(text[i])
        elif 'i' in text[i]:
            text.replace('i','j')
            text[i] = complex(text[i])

    while len(text)!=1:

        if '(' in text:
            index = text.index('(')+2

            if text[index] == '*':
                text = multi(text)
            elif text[index] == '/':
                text = div(text)
            
            if text[index] == '+':
                text = plus(text)
            elif text[index] == '-':
                text = minus(text)

            text.remove('(')
            text.remove(')')
       
        else:
            if '*' in text:
                text = multi(text)
            elif '/' in text:
                text = div(text)
            
            if '+' in text:
                text = plus(text)
            elif '-' in text:
                text = minus(text)

    await update.message.reply_text (f'result = {text[0]}')
    log('result', text[0])



