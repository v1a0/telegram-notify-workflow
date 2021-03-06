from misc import bot
from settings import CHAT_IDS, REPO, ACTOR, BASE_REF, HEAD_REF, REF
from requests import get

push = 'refs/heads/v1a0-patch-1'


async def new_pull_request():
    pr_number = REF.split('/')[-2]
    url = f"https://api.github.com/repos/{REPO}/pulls/{pr_number}"

    # url = f"https://api.github.com/repos/v1a0/sqllex/pulls/20"

    data = get(url).json()

    print(f"{url=}")
    print(f"{data=}")

    if isinstance(data, list):
        data = data[0]

    pull_request = data
    title = pull_request.get('title')
    description = pull_request.get('body')
    link = pull_request.get('url')
    auto_merged = pull_request.get('auto_merge')

    msg_about = f"""
🔀 NEW PULL REQUEST
↪️ {BASE_REF}/{HEAD_REF}
👨‍💻 {ACTOR}

{title if title else '< untitled >'}

About:
{description if description else "< empty >"}

Link:
{link}

Auto merged: {auto_merged}
"""

    for chat_id in CHAT_IDS:
        await bot.send_message(chat_id, msg_about)
