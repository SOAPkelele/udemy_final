from io import BytesIO

from aiogram import types
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def convert_to_video_note(message: types.Message):
    save_to_io = BytesIO()
    await message.video.download(destination=save_to_io)
    await message.answer_video_note(InputFile(save_to_io), length=50)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_document_id(message: types.Message):
    title = message.document.file_name
    await message.document.download(destination=f"documents/{title}")
    # await bot.send_document(chat_id=message.chat.id, document=f"documents/{title}")
    await bot.send_document(chat_id=message.chat.id, document=InputFile(f"documents/{title}",
                                                                        filename=f"new_name_{title}"))

