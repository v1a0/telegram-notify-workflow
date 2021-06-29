# About
![img1](https://user-images.githubusercontent.com/54343363/123735091-c2e86100-d8c8-11eb-8886-2f73007b09a7.png) ![img2](https://user-images.githubusercontent.com/54343363/123735250-16f34580-d8c9-11eb-9b21-665865ddced3.png)


# How to use

## Create new workflow

Create in you github repo file in this path `.github/workflows/telegram-notification.yml` (or clone it fom this one repo)

Enter this script into it

```yml
# This workflow will send notification about new releases in selected telegram chats
# Read more here https://github.com/v1a0/telegram-notify-workflow

name: Telegram notifications

on:
  release:
    types: [created]
  push:
    branches:
      - main
      - dev
      - 'dev/**'
  pull_request:
    branches:
      - main
      - dev
      - 'dev/**'

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
      run: |
        cd telegram-notify-workflow
        python bot.py

```

## setups
Open settings of your repo on github:

`https://github.com/__username__/__repo__/settings`

Enter you username and repo-name instead of `__username__` and `__repo__`

Go to "Secrets" folder and create 2 new repository secrets
```shell
# 1'st one
name: "TG_API_TOKEN"
value: (api token to your bot)

# 2'nd
name: "TG_CHAT_IDS"
value: (chat id`s with spaces between them)
```

Save it. Release a new version or make pr and enjoy!
