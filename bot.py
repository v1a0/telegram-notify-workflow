from misc import dp
from aiogram import executor
from settings import *
import handlers as event


async def new_event():

    if EVENT not in ['pull_request', 'push', 'release']:
        return

    print(str(EVENT) == 'release')

    if str(EVENT) in 'release':
        await event.new_release()

    print(str(EVENT) == 'pull_request')

    if str(EVENT) in 'pull_request':
        await event.new_pull_request()



if __name__ == '__main__':
    print(EVENT)
    executor.start(dp, new_event())


