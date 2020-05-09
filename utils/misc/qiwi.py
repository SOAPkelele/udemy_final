from dataclasses import dataclass
from datetime import datetime, timedelta

import pyqiwi

from data.config import QIWI_TOKEN, WALLET_QIWI
import uuid

wallet = pyqiwi.Wallet(token=QIWI_TOKEN, number=WALLET_QIWI)


class NoPaymentFound(Exception):
    pass


class NotEnoughMoney(Exception):
    pass


@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())

    def check_payment(self):
        for tx in wallet.history(rows=50, start_date=datetime.now() - timedelta(days=2))["transactions"]:
            if tx.comment:
                if str(self.id) in tx.comment:
                    if float(tx.total.amount) >= float(self.amount):
                        return True
                    else:

                        raise NotEnoughMoney

        else:
            raise NoPaymentFound
