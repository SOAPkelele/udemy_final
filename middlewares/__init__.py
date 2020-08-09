from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware
from .chatbaser import ChatbaseMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ChatbaseMiddleware())
