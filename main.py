import logging
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
import pytz

# === Налаштування ===
BOT_TOKEN = '8434126197:AAGbQ5Ki6B1TFSI_GCD_aXbPvRgxNlh-MRw'
CHAT_ID = '484670697'
START_DATE = datetime.date(2025, 1, 22)
TOTAL_DAYS = int(2.8 * 365)  # 2,8 роки
SEND_HOUR = 13

# === Логування ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# === Прогрес-бар ===
def make_progress_bar(percent, length=20):
    filled = int(length * percent / 100)
    return '█' * filled + '░' * (length - filled)

# === Повідомлення ===
def send_update():
    today = datetime.date.today()
    days_passed = (today - START_DATE).days
    days_left = TOTAL_DAYS - days_passed
    percent = max(0, min(100, int((days_passed / TOTAL_DAYS) * 100)))
    weeks_passed = days_passed // 7
    bar = make_progress_bar(percent)

    text = (
        f"⌛ Пройшло: {weeks_passed} тижнів\n"
        f"📅 Залишилось: {max(0, days_left)} днів\n"
        f"{bar} {percent}%"
    )

    try:
        bot.send_message(chat_id=CHAT_ID, text=text)
        logger.info("Повідомлення надіслано")
    except Exception as e:
        logger.error(f"Помилка надсилання: {e}")

# === Запуск бота ===
bot = Bot(token=BOT_TOKEN)
scheduler = BackgroundScheduler()
scheduler.add_job(
    send_update,
    'cron',
    day_of_week='sun',
    hour=SEND_HOUR,
    minute=0,
    timezone=pytz.timezone('Europe/Sofia')
)
scheduler.start()

# === Одразу надсилає тестове повідомлення ===
send_update()

logger.info("Бот запущений. Очікування...")

# === Підтримка роботи
import web  # ⬅️ додай ось сюди, перед циклом while

while True:
    time.sleep(60)
