from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

html_text = "\n".join(
    [
        "Привет, " + hbold("Костя!"),
        "Как говорится:",
        hitalic("Бояться надо не смерти, а пустой жизни."),
        "",
        "Но мы сейчас не об этом. " + hstrikethrough("Что тебе нужно?"),
        "Этот текст с HTML форматированием. Почитать об этом можно " + hlink("тут",
                                                                             "https://core.telegram.org/bots/api#formatting-options"),
        hunderline("Внимательно прочти и используй с умом!"),
        "",
        "Пример использования - ниже:",
        hcode("""<b>bold</b>, <strong>bold</strong>
<i>italic</i>, <em>italic</em>
<u>underline</u>, <ins>underline</ins>
<s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
<b>bold <i>italic bold <s>italic bold strikethrough</s> <u>underline italic bold</u></i> bold</b>
<a href="http://www.example.com/">inline URL</a>
<a href="tg://user?id=123456789">inline mention of a user</a>
<code>inline fixed-width code</code>
<pre>pre-formatted fixed-width code block</pre>
<pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>""")
    ])


@dp.message_handler(Command("parse_mode_html"))
async def show_parse_mode(message: types.Message):
    await message.answer(html_text, parse_mode=types.ParseMode.HTML)
