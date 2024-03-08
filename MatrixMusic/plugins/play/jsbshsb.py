import asyncio
import random
import os
import time
import requests
from random import  choice, randint
from pyrogram import Client, filters
from MatrixMusic.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from MatrixMusic import app


@app.on_message(
    command(["سورس","السورس","المطور"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://www7.0zz0.com/2024/02/28/05/415560079.jpg",
        caption=f"""-| مطور السورس \n-| قناة المطور""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"https://t.me/K_o_c_1"),
                ],
                [
                   InlineKeyboardButton(
                        "- قناة المطور ", url=f"https://t.me/K_o_c_3"),
                ],       
            ]
        ),
    )
