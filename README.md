# shopbot

shopping list discord bot

## Purpose

The Alexa and Google Home smart speakers are annoying, they don't allow you to remove an item from a shopping list and they don't check for duplicates.  They are slow to produce a full list when asked.  This project replaces that functionality with a discord bot.  The future is now.

## Pre Requisites

* A server, an app, a bot, and a token
  * You can follow this [dev dunegon tutorial](https://www.devdungeon.com/content/make-discord-bot-python)
* Python
  * For windows, Python [from python.org](https://www.python.org/downloads/)
  * For linux, you should already have python installed. If not try:

```bash
apt-get install python3
apt-get install python3-pip
```

## Startup

```bash
# pip install discord.py==0.16.12
# git clone https://github.com/juanino/shopbot.git
# cp shopbotconfig_example.py shopbotconfig.py
# ./shopBot.py
```

## Usage in discord

Try !hello first, then add some items and list.

```discord
!help
shopBot BOT Today at 3:54 PM
Help commands:
                    !hello - test to make sure the bot is listening
                    !add [some item name] - add an item
                    !list - list items in the shopping list
                    !remove [some item name] - remove a specific item by name
                    !pop [item number] - remove a specific item
                    !save - force list to be saved. not necessary except for debugging
                    !total - how many items are on the list
```

## Use with QR scanner
You can create a printout for use with a USB scanner gun with qrcode_maker.py by
copying the sample_grocerysheet.py to grocerysheet.py and running it. The tool will output
a scan_sheet.html which you can print out and scan.  These are readable with a standard QR gun like
[this one](https://www.amazon.com/Tera-Wireless-Portable-Handheld-Vibration/dp/B07M68LS2N)


## Issues

* You definitely need the specific version of discord.py.  I have no idea why.
* When using control + c in windows it takes a long time for the program to exit. use !crash in discord instead to tell the bot to shutdown

## Credit

* Mostly I credit this tutorial: <https://www.devdungeon.com/content/make-discord-bot-python>
* Icons used in the sample sample_grocerysheet.py are from [icons8](https://icons8.com/)
