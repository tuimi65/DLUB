import os
import sys
import shutil


from pyrogram import Client, filters

@Client.on_message(filters.me and filters.command(["purge"]))
async def purge(client, message):
    if len(message.command) != 2:
        text = "Specify File to Delete"
    else:
        file = 'downloads' + message.command[1]
        if os.path.exists(file):
            os.remove(file)
            text = f"{message.command[1]} Deleted Successfuly"
        else:
            text = "File Does Not Exist"
        await message.edit_text(text)
         
             

@Client.on_message(filters.me and filters.command(["purgeall"]))
async def purgeall(client, message):
    try:
        shutil.rmtree("downloads")
        text = "Purged All Cache!"
    except OSError as e:
        text = "Folder Not Found!"
    await message.edit_text(text)
        