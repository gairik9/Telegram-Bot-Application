import asyncio
import os
import sys
import time
from telethon import TelegramClient, events, utils

# Phone Number Acoount Registered 
name = "+916000218006"
# Account API ID
api_id = 27058605
# Account API Hash
api_hash = "c5d7b09f6eea3c2fd71f6278cf9f7bc8"

def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

# Session name, API ID and hash to use; loaded from environmental variables
SESSION = os.environ.get('TG_SESSION', 'gui')
API_ID = 27058605
API_HASH = "c5d7b09f6eea3c2fd71f6278cf9f7bc8"

async def main(cha):
    client = TelegramClient(SESSION, API_ID, API_HASH)
    try:
        await client.connect()
    except Exception as e:
        print('Failed to connect', e, file=sys.stderr)
        return
    await client.send_code_request(phone="+916000218006")
    code = input("Enter Code :")
    await client.sign_in(code=code)
    # Connects to the Telegram Client
    try:
        await client.connect()
    except OSError:
        print('Failed to connect')
        os._exit()
    else :
        print('Connect Successful')

    # Getting Channel Name from User Input
    channels = cha.split()


    for channel in channels:    
        # async for message in client.iter_messages(channel,reverse=True):
        #    # message_text[str(message.date)] = message.text
        #     message_text['text'] = str(message.text)
        #     message_text['id'] = str(message.id)
        #     message_text['peer_id'] = str(message.peer_id)
        #     message_text['date'] = str(message.date)
        #     message_text['message'] = str(message.message)
        #     message_text['out'] = str(message.out)
        #     message_text['mentioned'] = str(message.mentioned)
        #     message_text['media_unread'] = str(message.media_unread)
        #     message_text['silent'] = str(message.silent)
        #     message_text['post'] = str(message.post)
        #     message_text['from_scheduled'] = str(message.from_scheduled)
        #     message_text['legacy'] = str(message.legacy)
        #     message_text['edit_hide'] = str(message.edit_hide)
        #     message_text['pinned'] = str(message.pinned)
        #     message_text['noforwards'] = str(message.noforwards)
        #     message_text['fwd_from'] = str(message.fwd_from)
        #     message_text['via_bot_id'] = str(message.via_bot_id)
        #     message_text['reply_to'] = str(message.reply_to)
        #     message_text['media'] = str(message.media)
        #     message_text['reply_markup'] = str(message.reply_markup)
        #     message_text['entities'] = str(message.entities)
        #     message_text['views'] = str(message.views)
        #     message_text['forwards'] = str(message.forwards)
        #     message_text['replies'] = str(message.replies)
        #     message_text['edit_date'] = str(message.edit_date)
        #     message_text['post_author'] = str(message.post_author)
        #     message_text['grouped_id'] = str(message.grouped_id)
        #     message_text['reactions'] = str(message.reactions)
        #     message_text['restriction_reason'] = str(message.restriction_reason)
        #     message_text['ttl_period'] = str(message.ttl_period)   

        #     # Creating a json object with the required fields
        #     json_obj = json.dumps(message_text, indent = 4)

        #     # Dumping json object to the json file
        #     with open("file.json", "a") as outfile:
        #         outfile.write(json_obj)


        # Show all user IDs in a chat
        async for user in client.iter_participants(channel):
            print(user.id)
            print(user.username)
            print(user.first_name)
            print(user.last_name)
            print(user.phone)
            #print(user.photo)
            #print(user.status)
            # print(user.is_self)
            # print(user.contact)
            # print(user.mutual_contact)
            # print(user.deleted)
            # print(user.bot)
            # print(user.bot_chat_history)
            # print(user.bot_nochats)
            # print(user.verified)
            # print(user.restricted)
            # print(user.min)
            # print(user.bot_inline_geo)
            # print(user.support)
            # print(user.apply_min_photo)
            # print(user.fake)
            # print(user.bot_attach_menu)
            # print(user.premium)
            # print(user.attach_menu_enabled)
            # print(user.access_hash)
            # print(user.bot_info_version)
            # print(user.restriction_reason)
            # print(user.bot_inline_placeholder)
            # print(user.lang_code)
            # print(user.emoji_status)
            # print(user.usernames)

    print("Write Data Successful")
    

def run(cha):
    asyncio.run(main(cha))