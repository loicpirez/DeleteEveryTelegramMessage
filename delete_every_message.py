#!/usr/bin/env python3

from telethon import TelegramClient
from telethon import utils
from telethon.utils import get_display_name
from telethon.tl.functions.messages import DeleteMessagesRequest

api_id = int(os.environ.get('TELEGRAM_API_ID'))
api_hash = os.environ.get('TELEGRAM_API_HASH')

client = TelegramClient(os.environ.get('TELEGRAM_API_NAME'), api_id, api_hash)
client.start()

for val in client.get_dialogs(limit=None):
    for message in client.iter_messages(val.id, limit=None):
      result = client.invoke(DeleteMessagesRequest([ message.id ], True))
