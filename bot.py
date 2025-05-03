import os
import logging
import random
from PIL import Image, ImageDraw, ImageFont
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
WORDS = ["Sunset", "Adventure", "Memory", "Journey", "Smile", "Dream", "Wander", "Freedom", "Hope", "Bloom"]

def apply_polaroid_effect(image_path, output_path):
    image = Image.open(image_path)
    border_size = 50
    new_width = image.width + border_size * 2
    new_height = image.height + border_size * 3
    polaroid = Image.new('RGB', (new_width, new_height), 'white')
    polaroid.paste(image, (border_size, border_size))

    draw = ImageDraw.Draw(polaroid)
    font = ImageFont.load_default()
    text = ' '.join(random.sample(WORDS, 2))
    text_width, _ = draw.textsize(text, font=font)
    text_position = ((new_width - text_width) / 2, new_height - border_size + 10)
    draw.text(text_position, text, fill='black', font=font)
    polaroid.save(output_path)

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    photo_file = await photo.get_file()
    input_path = "input.jpg"
    output_path = "polaroid.jpg"
    await photo_file.download_to_drive(input_path)
    apply_polaroid_effect(input_path, output_path)
    await update.message.reply_photo(photo=open(output_path, "rb"))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.run_polling()
