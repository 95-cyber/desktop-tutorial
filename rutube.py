import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Список ссылок на уроки в RuTube
LESSONS = [
    "https://rutube.ru/video/private/62671099b18c5eb5204b2db81df79ab2/?p=WCxaTpCHCrq5XHQEif8S6g/",
    "https://rutube.ru/video/private/af2fbe0ccab3c326160eae7e618cbed4/?p=lpB3E3vEXQRO0mmN_W36nw/",
    "https://rutube.ru/video/private/0820f49ab9a497fad0f4c20a60b7713d/?p=gR73Ie6a14QWvu1IO-jiRw/",
"https://rutube.ru/video/private/81eac1bb3e7f635bdb9a631532cd238b/?p=iu2WPhpBkRz50mKeguM3ww/",
"https://rutube.ru/video/private/868c51e1259327ca2b1101fa4b3e4178/?p=JPPhkFq4OMSF3WOwP2TOIQ/",
"https://rutube.ru/video/private/2fa987de2a26cbde80795c8f482ea206/?p=qBI2eUnxBFKxV-EC7Xqasg/",
"https://rutube.ru/video/private/76761642aa8abde60de20027f5f78537/?p=9AMi-qFJdJGp81C-_c9ohA/",
"https://rutube.ru/video/private/af414715fbfe20dfa6f602ebb60d6d06/?p=qbI7yCsI95u73KdsWWuKEg/",
"https://rutube.ru/video/e616b8eeaec11e4fc19c68f3d181647f//",
"https://rutube.ru/video/private/85caad6478ebb50fc1ade5e20b193da8/?p=s1V-pb_cfr-mEwQbVzQcuA/",
"https://rutube.ru/video/e27ef3dd920f4ecf5c284e89a55f6fe6//",
"https://rutube.ru/video/private/3c79680b86f850253f33e7bf03b3decf/?p=692vk2z9UJC2mzuwk0k-Xw/",
    # Добавьте свои ссылки на уроки
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот, который выдает ссылки на уроки в RuTube. "
        "Используй команду /lessons для получения списка уроков."
    )

async def lessons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not LESSONS:
        await update.message.reply_text("Список уроков пуст!")
        return

    # Создаем кнопки для каждого урока
    keyboard = [
        [InlineKeyboardButton(f"Урок {i+1}", url=link)]
        for i, link in enumerate(LESSONS)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выберите урок, нажав на кнопку ниже:",
        reply_markup=reply_markup
    )

def main():
    BOT_TOKEN = "8476332708:AAGxLQqGqRidMZwfa_5C2Mx5B0efrVkyxpo"

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("lessons", lessons))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
