#!/usr/bin/python3
import discord
import pickle
import pprint
import shopbotconfig as cfg

TOKEN = cfg.token

client = discord.Client()
shoppingList = []
pp = pprint.PrettyPrinter(indent=4)


# open the shopping list pickle
try:
    with open('list.pickle','rb') as f:
        shoppingList = pickle.load(f)
except:
    print("Could not open shopping list pickle file")
    print("using a blank one")
    print(type(shoppingList))

def saveList(shoppingList):
    with open('list.pickle','wb') as f:
        pickle.dump(shoppingList, f)
    print("Saved to file")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    else:
        print("message from " + str(message.author))
        print("message was: " + str(message.author) +  "->" + str(message.content))

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message) + 'I am the shopBot'
        await client.send_message(message.channel, msg)
        print("got a hello command")
    elif message.content.startswith('!list'):
        print("got a list command")
        pp.pprint(shoppingList)
        msg = 'You have the following items on the list:'
        await client.send_message(message.channel,msg)
        x = 0
        msg = ""
        for item in shoppingList:
            print(str(x)+item)
            msg = msg +  "#" + str(x)+ ".  " + item + "\n"
            # await client.send_message(message.channel,msg)
            x = x + 1 
        await client.send_message(message.channel,msg)
        await client.send_message(message.channel,'end of list')
    elif message.content.startswith('!add'):
        itemToAdd = str(message.content)
        print('add msg is->' + itemToAdd)
        itemToAdd = itemToAdd.replace('!add','')
        print('item->' + itemToAdd)
        msg = 'Adding ' + itemToAdd + ' to list'
        await client.send_message(message.channel,msg)
        if shoppingList.count(itemToAdd) > 0:
            print("Duplicate")
            msg = 'Item ' + itemToAdd + ' is a duplicate. Ignoring you.'
            await client.send_message(message.channel,msg)
        else:
            shoppingList.append(itemToAdd)
        pp.pprint(shoppingList)
        saveList(shoppingList)
    elif message.content.startswith('!remove'):
        itemToRemove = str(message.content)
        print('remove msg is->' + itemToRemove)
        itemToRemove = itemToRemove.replace('!remove','')
        print('item->' + itemToRemove)
        msg = 'Removing ' + itemToRemove + ' from the list'
        await client.send_message(message.channel,msg)
        print(type(itemToRemove))
        try:
            shoppingList.remove(itemToRemove)
            msg = "Successfully removed" + itemToRemove
            await client.send_message(message.channel,msg)
        except:
            msg = itemToRemove + " not on list"
            await client.send_message(message.channel,msg)
        pp.pprint(shoppingList)
        saveList(shoppingList)
    elif message.content.startswith('!crash'):
        exit()
    elif message.content.startswith('!save'):
        print("forcing save to disk")
        pp.pprint(shoppingList)
        saveList(shoppingList)
        msg = "ok, I saved your file to disk on the bot machine"
        await client.send_message(message.channel,msg)
    elif message.content.startswith('!help'):
        msg = """ Help commands: 
                    !hello - test to make sure the bot is listening
                    !add [some item name] - add an item
                    !list - list items in the shopping list
                    !remove [some item name] - remove a specific item by name
                    !pop [item number] - remove a specific item
                    !save - force list to be saved. not necessary except for debugging
                    !total - how many items are on the list
        """
        await client.send_message(message.channel,msg)
    elif message.content.startswith('!pop'):
        itemToRemove = str(message.content)
        print('remove msg is->' + itemToRemove)
        itemToRemove = itemToRemove.replace('!pop','')
        print('item->' + itemToRemove)
        msg = 'Removing #' + itemToRemove + ' ' + shoppingList[int(itemToRemove)] + ' from the list' 
        await client.send_message(message.channel,msg)
        try:
            shoppingList.pop(int(itemToRemove))
            msg = "Successfully removed" + itemToRemove
            await client.send_message(message.channel,msg)
        except:
            msg = "item not on list"
            await client.send_message(message.channel,msg)
        pp.pprint(shoppingList)
        saveList(shoppingList)
    elif message.content.startswith('!total'):
        count = len(shoppingList)
        msg = 'You have ' + str(count) + ' items on your list'
        await client.send_message(message.channel,msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    msg = "Bot startup complete"
    await client.send_message(client.get_channel(cfg.bot_channel_id), msg)

client.run(TOKEN)

