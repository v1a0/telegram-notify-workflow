from misc import bot
from settings import CHAT_IDS, REPO, ACTOR, SHA, REF, PM


async def new_push():
    emoji = 'π‘ππ₯π₯ͺπ­πβπ½πΈπ'[int(SHA, 16) % 10]
    msg_about = f"""
π NEW PUSH
βͺοΈ {REF}
π¨βπ» {ACTOR}

#οΈβ£ [{SHA[:7]}](https://github.com/{REPO}/commit/{SHA}) {emoji}
"""

    for chat_id in CHAT_IDS:
        await bot.send_message(chat_id, msg_about, parse_mode=PM)
