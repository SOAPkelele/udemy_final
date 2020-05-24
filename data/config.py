import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
DATABASE = os.getenv("DATABASE")
admins = [
    362089194
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

POSTGRES_URI = f"postgres://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
