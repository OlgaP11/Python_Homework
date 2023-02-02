from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from calc import main as calc, multi, plus, minus


app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("calc", calc)) 

print('ready')

app.run_polling()