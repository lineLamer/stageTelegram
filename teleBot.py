from aiogram import Bot
from telegram import *
from aiogram.types import Message
import asyncio

import canalBot
from canalBot import *
import librairie as lib
#TELEGRAM_BOT_TOKEN = '7181142934:AAGxxLdS7hZ4LpwUdh-chNPcxko86I0_u_Q'


CHAT_ID = canalBot.main()
print(CHAT_ID)
print(f'//// Send Messages to TELEGRAM...')

messages = ['This is my 000000 message, be careful!']

bot = Bot(token=lib.bot_token)

async def send_message(text, chat_id):
    bot = await client.
    await bot.send_message(chat_id=chat_id, text=text)

async def run_bot(messages):
    text = '\n'.join(messages)
    await send_message(text, CHAT_ID)

#if messages:
#asyncio.run(run_bot(messages))
async def main():
    #messages = ['This is my third message, be careful!']
    await run_bot(messages)
    #await bot.close()


if __name__ == '__main__':
    asyncio.run(main())



print(f'//// Messages sent to TELEGRAM...')



#--------------------------------------------------



