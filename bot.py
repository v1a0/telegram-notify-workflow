from misc import dp
from handlers import *
from aiogram import executor
import logging
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, help='Code name of action to run')
    args = parser.parse_args()

    print(args)

    if args.action:
        logging.info(args.action)
        executor.start(dp, new_release())

    # executor.start_polling(dp, skip_updates=True)

