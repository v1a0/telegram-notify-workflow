from misc import bot
from settings import CHAT_IDS, REPO, PM, ACTOR
from requests import get


async def new_release():
    # url = f"https://api.github.com/repos/{REPO}/releases"
    url = f"https://api.github.com/repos/sqllex/releases"
    data = get(url).json()

    print(data)

    last_release = data[0]
    name = last_release.get('name')
    description = last_release.get('body')
    link = last_release.get('html_url')

    msg_about = f"""
NEW RELEASE (by {ACTOR})

{name}

About:
{description}

Link:
{link}  
"""

    msg_upd = f"""
Update:
```
pip install -U {REPO.split('/')[1]}
```
"""

    for chat_id in CHAT_IDS:
        await bot.send_message(chat_id, msg_about)
        await bot.send_message(chat_id, msg_upd, parse_mode=PM)

