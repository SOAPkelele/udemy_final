from dataclasses import dataclass
from datetime import datetime

import blockcypher as bs
from dateutil.tz import tzutc

from data import config


class AddressDetails:
    def __init__(self,
                 address: str,
                 total_received: int,
                 total_sent: int,
                 balance: int,
                 unconfirmed_balance: int,
                 unconfirmed_txrefs: list, **kwargs):
        self.address = address
        self.total_received = total_received
        self.total_sent = total_sent
        self.balance = balance
        self.unconfirmed_balance = unconfirmed_balance
        self.unconfirmed_txrefs = unconfirmed_txrefs


class NoPaymentFound(Exception):
    pass


class NotConfirmed(Exception):
    pass


@dataclass
class Payment:
    amount: int
    created: datetime = None
    success: bool = False

    def create(self):
        self.created = datetime.now(tz=tzutc())

    def check_payment(self):
        details = bs.get_address_details(address=config.WALLET_BTC, api_key=config.BLOCKCYPHER_TOKEN)
        ad = AddressDetails(**details)
        for transaction in ad.unconfirmed_txrefs:
            if transaction["value"] == self.amount:
                if transaction["received"] > self.created:
                    if transaction["confirmations"] > 0:
                        return True
                    else:
                        raise NotConfirmed
        else:
            raise NoPaymentFound
