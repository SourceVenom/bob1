import asyncio

import random

from MatrixMusic import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





txt = [


"ها عايز اي 🙄",
"ايوااا جااااي 😂",
"عاوزني اشقطلك مين يروحي 🥺",
"ايوة قول عاوز اي 🤔",
"قلب البوت 🥺",
"يعم تعبتنا معاك 🙁",
"استنا يعم بشقط وجايبك علطول 😂",
"فينوم بيحبك يسطا وربنا بس نديلي بي فينوم احسن 🥺" 
        ]


        


@app.on_message(filters.command(["بوت","يا بوت"], ""))

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
