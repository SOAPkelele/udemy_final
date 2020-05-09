import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
BLOCKCYPHER_TOKEN = os.getenv("BLOCKCYPHER")
WALLET_BTC = os.getenv("wallet")
REQUEST_LINK = "bitcoin:{address}?" \
               "amount={amount}" \
               "&label={message}"

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
