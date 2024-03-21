from pyrogram import Client as Bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """Hello {},
I am a media background remover bot. \
Send me a photo I will send the photo without background.

Made by @iMediaUniverse"""

HELP_TEXT = """--**More Help**--

- Just send me a photo or video
- I will download it
- I will send the photo or video without background

Made by @iMediaUniverse"""

ABOUT_TEXT = """**About Me**

- **Bot :** `Backround Remover Bot`
- **Developer :** [Telegram](https://telegram.me/Mehitmannub)
- **Source :** [Click here](https://github.com)
- **Language :** [Python 3](https://python.org)
- **Library :** [Pyrogram](https://pyrogram.org)"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ],
        [
            InlineKeyboardButton('Feedback', url='https://telegram.me/iMediaSupport')
        ]
    ]
)

HELP_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

ABOUT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Join Channel', url='https://telegram.me/iMediaSupport')
        ]
    ]
)


@Bot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await start(bot, update, cb=True)
    elif update.data == "help":
        await help(bot, update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update, cb=False):
    text=START_TEXT.format(update.from_user.mention)
    if cb:
        await update.message.edit_text(
            text=text,
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )


@Bot.on_message(filters.private & filters.command(["about"]))
async def about(bot, update, cb=False):
    if cb:
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
