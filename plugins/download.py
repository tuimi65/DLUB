from pyrogram import Client, filters

@Client.on_message(filters.me and filters.command("lel"))
async def lel(client, message):
    msg = message.reply_to_message
    file = msg.media
    
    if not file:
        await message.edit_text("Not A File Bruhh!")
    else:
        file = await msg.download(in_memory=False)
        await client.send_document("me", file)
        await message.edit_text("Uploaded!")