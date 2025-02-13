#---------------------------------------------------

import requests
from charset_normalizer.md__mypyc import exports
from telegram import Bot
from telethon import TelegramClient
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.channels import CreateChannelRequest, InviteToChannelRequest
import asyncio
from telegram import Bot

import librairie as lib


bot = Bot(token=lib.bot_token)
channel_id = 0
client = TelegramClient(lib.session, lib.api_id, lib.api_hash)


async def create_channel_and_add_users():

    print('hello, je suis 1111')
    await client.start(str(lib.phone_number))

    print('hello, je suis 6666')
    result = await client(CreateChannelRequest(
        title='CarteSoft',
        about='This is a description of my new channel',
        megagroup=False
    ))

    print('hello, je suis 5555')
    global channel_id
    channel_id = result.chats[0].id
    print('------channel_id--------', channel_id)

    users = []
    for user_id in lib.user_ids:  # Correction ici
        try:
            entity = await client.get_input_entity(int(user_id))
            users.append(entity)
        except Exception as e:
            print(f"Erreur lors de la récupération de l'utilisateur {user_id}: {e}")

    if users:
        await client(InviteToChannelRequest(channel_id, users))

    invite_link = await client(ExportChatInviteRequest(channel_id))
    print(f'Channel created successfully! Invite link: {invite_link.link}')

    return channel_id

async def send_notification(channel_id, message):
    print('hello, je suis 2222')

    #bot = '7181142934:AAGxxLdS7hZ4LpwUdh-chNPcxko86I0_u_Q'
    bot = await client._get_entity_from_string(f'@{lib.bot_name}')
    #await client.get_entity(f'@{lib.bot_name}')
    print(bot)
    chat = channel_id
    try:
        await client(InviteToChannelRequest(chat, bot))

        print('hello, cest reussi')
    except Exception as e:
        print('--------- *** erreur d ajout du bot *** -------------')
    print('hello, je suis 33333')
    await bot.send_message(chat_id=channel_id, text=message)
    print('hello, je suis 777')


# async def send_notification(channel_id, message):
#     # Ajoutez le bot au canal
#     bot_entity = await client.get_entity(f'@{lib.bot_username}')
#     await client(InviteToChannelRequest(channel_id, [bot_entity]))
#
#     # Envoyez un message au canal
#     await bot.send_message(chat_id=f'-100{channel_id}', text=message)
#     print('hello, je suis 2222')

async def main():
    print('hello, je suis 000')
    channel_id = await create_channel_and_add_users()

    print('------channel_id--------', channel_id)
    await send_notification(channel_id, 'This is a notification message.')
    return channel_id


if __name__ == '__main__':
    client.loop.run_until_complete(main())