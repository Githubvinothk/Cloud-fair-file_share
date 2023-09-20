#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/dhanusha_3'>This Person</a>\n○ Language : <code>Tamil🥰</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {version}</a>\n○ Source Code : <a href='https://t.me/TDM_FilmDepot'>Click here</a>\n○ Channel : @Team_TDM\n○ Support Group : <a href='https://t.me/+AT8PMERSstNhNTc1'>Join Here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
