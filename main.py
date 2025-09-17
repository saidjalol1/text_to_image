import os
import uuid
import requests
from configs import image_generator, settings
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command from user"""
    await update.message.reply_text("👋 Salom , Menga qanday rasm xohlashingizni tasvirlang va men sizga uni generatsiya qilib beraman")


async def handle_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    await update.message.reply_text("🎨 Rasmni tayyorlayapman iltimos biroz kuting")

    image_path = image_generator.generate_image(prompt)
    if image_path:
        await update.message.reply_photo(photo=open(image_path, "rb"), caption="Mana siz xohlagan rasm 🚀")
    else:
        await update.message.reply_text("⚠️ Juda charchadim iltimos keyin urinib koring ishiz zarur bolmasa")

def main():
    TOKEN = settings.TOKEN
    if not TOKEN:
        raise ValueError("⚠️ Juda charchadim iltimos keyin urinib koring ishiz zarur bolmasa")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_prompt))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
