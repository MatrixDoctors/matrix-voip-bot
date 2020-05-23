'''
Documentation, License etc.

@package MatrixVoipBot
'''
from importlib import util
import asyncio
from nio import (AsyncClient, SyncResponse, RoomMessageText, CallEvent)

async def message_cb(room, event):
    print(
        "Call received for room {} | {}: {}".format(
            room.display_name, room.user_name(event.sender), event
        )
    )

async def main():
    client = AsyncClient("https://matrix.org", "@testvoipbot:matrix.org")
    client.add_event_callback(message_cb, CallEvent)

    await client.login("5qmeL9o9fcWJEKV3W3VC")
    await client.sync_forever(timeout=30000)

asyncio.get_event_loop().run_until_complete(main())

