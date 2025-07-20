from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os
TOKEN = os.getenv("7633243613:AAGDrXirTcPYotF17SgHQAZQPEI78NbEFUQ")


# 🔑 Replace with your actual bot token
# TOKEN = "7633243613:AAGDrXirTcPYotF17SgHQAZQPEI78NbEFUQ"

# Vocabulary list
vocab = {
    "Maaf": "Sorry",
    "Permisi": "Excuse me",
    "Tolong": "Help",
    "Maukah": "Would you like",
    "Bisakah": "Can you",
    "Gerah": "Hot",
    "Cuaca": "Weather",
    "Macet": "Jammed",
    "Sepi": "Quiet",
    "Ramai": "Noisy",
    "Pesan": "Message",
    "Menelepon": "Call",
    "Sibuk": "Busy",
}

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Ketik /quiz untuk memulai kuis kosakata.")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah:\n/start - Mulai bot\n/quiz - Kuis\n/answer [jawaban] - Jawabanmu")

# /quiz
async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    word, meaning = random.choice(list(vocab.items()))
    context.user_data["current_word"] = word
    await update.message.reply_text(f"Apa arti dari kata: '{word}'?\n(jawab dengan /answer kata_dalam_bahasa_inggris)")

# /answer your_answer
async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Ketik jawaban setelah perintah. Contoh: /answer help")
        return

    user_input = ' '.join(context.args).strip().lower()
    current_word = context.user_data.get("current_word")

    if not current_word:
        await update.message.reply_text("Ketik /quiz dulu untuk memulai.")
        return

    correct_answer = vocab[current_word].lower()

    if user_input == correct_answer:
        await update.message.reply_text("✅ Benar!")
    else:
        await update.message.reply_text(f"❌ Salah. Jawaban yang benar: {vocab[current_word]}")

    context.user_data["current_word"] = None  # Reset

# === START BOT ===
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("answer", answer))

print("✅ Bot is running...")
app.run_polling()
