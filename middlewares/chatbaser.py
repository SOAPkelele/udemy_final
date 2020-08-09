from aiogram import types
from aiogram.dispatcher.handler import current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware

from chatbase_track import AiogramChatBase
from data import config

aiogram_chat_base = AiogramChatBase(api_key=config.chatbase)


class ChatbaseMiddleware(BaseMiddleware):

    @staticmethod
    async def on_pre_process_message(message: types.Message, data: dict, *args, **kwargs):
        data["handled"] = False

    @staticmethod
    async def on_pre_process_callback_query(query: types.CallbackQuery, data: dict, *args, **kwargs):
        data["handled"] = False

    @staticmethod
    async def on_post_process_message(message: types.Message, *args, **kwargs):
        data = args[1]
        if not data.get('handled'):
            aiogram_chat_base.from_message(message=message, not_handled=True)

    @staticmethod
    async def on_post_process_callback_query(query: types.CallbackQuery, *args, **kwargs):
        data = args[1]
        if not data.get('handled'):
            aiogram_chat_base.from_callback_query(query=query, not_handled=True)

    @staticmethod
    async def on_process_message(message: types.Message, data: dict):
        handler = current_handler.get()
        if handler:
            handler_name = handler.__name__
            aiogram_chat_base.from_message(message=message,
                                           intent=handler_name)

    @staticmethod
    async def on_process_callback_query(query: types.CallbackQuery, data: dict):
        handler = current_handler.get()
        if handler:
            handler_name = handler.__name__
            aiogram_chat_base.from_callback_query(query=query,
                                                  intent=handler_name)
