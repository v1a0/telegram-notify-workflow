from misc import bot
from settings import CHAT_IDS, REPO, ACTOR
from requests import get

push = 'refs/heads/v1a0-patch-1'


async def new_pull_request():
    pr_number = 'refs/pull/1/merge'.split('/')[-2]

    # url = f"https://api.github.com/repos/{REPO}/pulls/{pr_number}"
    url = f"https://api.github.com/repos/v1a0/sqllex/pulls/20"
    data = get(url).json()

    print(data)

    pull_request = data[0]
    title = pull_request.get('title')
    description = pull_request.get('body')
    link = pull_request.get('url')
    auto_merged = pull_request.get('auto_merge')

    msg_about = f"""
NEW PULL REQUEST (by {ACTOR})

{title}

About:
{description}

Link:
{link}

Auto merged: {auto_merged}
"""

    for chat_id in CHAT_IDS:
        await bot.send_message(chat_id, msg_about)
