from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("CʜᴀᴛGPT", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q"),
    [InlineKeyboardButton("Tᴀɢ-Aʟʟ", callback_data="mplus HELP_TagAll"),
    [InlineKeyboardButton("Aᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("Sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search")],             
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
