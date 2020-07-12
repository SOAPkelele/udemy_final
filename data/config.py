import os

from dotenv import load_dotenv

load_dotenv()
# https://plugins.jetbrains.com/plugin/12798-tabnine
# https://qiwi.com/api
# https://qiwi.com/p2p-admin/transfers/api
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

QIWI_TOKEN = os.getenv("qiwi")
WALLET_QIWI = os.getenv("wallet")
QIWI_PUBKEY = os.getenv("qiwi_p_pub")

admins = [
    517563938
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
