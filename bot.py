from misc import dp
from aiogram import executor
from settings import *
import handlers as event


async def new_event():

    if EVENT not in ['pull_request', 'push', 'release']:
        return

    if EVENT == 'release':
        await event.new_release()

    if EVENT == 'pull_request':
        await event.new_pull_request()

    if EVENT == 'push':
        await event.new_push()

if __name__ == '__main__':
    executor.start(dp, new_event())


