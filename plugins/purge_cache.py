import os
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
        text = f"Folder Not Found! {e}"
    await message.edit_text(text)

@Client.on_message(filters.me and filters.command(["list"]))
def files(client, message):
    _list = os.listdir("downloads")
    try:
        dirstr = [(f"-> {x}") for x in _list].join("\n")
    except Exception:
        dirstr = "Nothing Here Yet"
    message.edit_text(dirstr)
        