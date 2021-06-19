# How to use

## cloning

Create in you repo file in this path `.github/workflows/telegram-notification.yml` (or clone it fom this repo)

Enter this script into it

```yml
# This workflow will send notification about new releases in selected telegram chats

name: Telegram notifications

on:
  release:
    types: [created]

jobs:
  telegram-bot:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python3.9
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Update pip
      run: |
        python -m pip install --upgrade pip
        
    - name: Clone repo, install requirements
      run: |
        git clone https://github.com/v1a0/telegram-notify-workflow.git ./telegram-notify-workflow
        cd telegram-notify-workflow
        python -m pip install -r requirements.txt
        
    - name: Run bot
      env:
        secrets.WF_API_TOKEN: ${{ secrets.WF_API_TOKEN }}
        secrets.WF_CHAT_IDS: ${{ secrets.WF_CHAT_IDS }}
        secrets.WF_REPO: "v1a0/telegram-notify-workflow"
      run: |
        cd telegram-notify-workflow
        python bot.py --action release

```

## setups
Find this line in this file:
```yml
secrets.WF_REPO: "v1a0/telegram-notify-workflow"
```
 You have to change ant type here you github `nickname/repo_name`
 For example my username here `v1a0` and my new repo `new_repo`, so this line be look like this:
 
```yml
secrets.WF_REPO: "v1a0/new_repo"
```

Then open setting your repo on github

`https://github.com/__username__/__repo__/settings`

Enter you username and repo-name instead of `__username__` and `__repo__`

Go to "Secrets" folder and create 2 new repository secrets
```shell
# 1'st one
name: "WF_API_TOKEN"
value: (api token to your bot)

# 2'nd
name: "WF_CHAT_IDS"
value: (chat id's with spaces between them)
```

Save it. Release a new version of your product and enjoy!