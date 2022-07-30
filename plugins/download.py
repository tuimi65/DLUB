from pyrogram import Client, filters

@Client.on_message(filters.me and filters.command("lel") and filters.reply)
async def lel(client, message, file=None):
    
    msg = message.reply_to_message
    if file == None:
        file = msg.media
    if not file:
        await message.edit_text("Not A File Bruhh!")
    else:
        file = await msg.download(in_memory=False)
        await client.send_document("me", file)
        await message.edit_text("Uploaded!")
        
@Client.on_message(filters.me and filters.command("lel"))
async def chatlink(client, message):
    if len(message.command) != 2:
        pass
    else:
        link = (message.command[1]).split('/')
        chatid = int(link[2])
        messageid = int(link[1])
        file = Client.get_messages(chatid, messageid)
        lel(client, message, file=file.media)
        
        
        
        