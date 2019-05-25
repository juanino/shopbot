#!/usr/bin/python3

from discord_webhook import DiscordWebhook
import sys
import shopbotconfig as cfg

url = cfg.webhook_safe

try:
    message = sys.argv[1]
except:
    print("no message passed, usage: ./send_discord blah")
    sys.exit(1)

webhook = DiscordWebhook(url=url, content=message)
webhook.execute()