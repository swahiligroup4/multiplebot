from botii import Bot0
import re
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton,ChatPermissions
from info import filters
from plugins.status import handle_admin_status
from plugins.database import db
from utils import get_filter_results, is_user_exist,User ,get_file_details,is_subscribed,add_user

@Bot0.on_message(filters.new_chat_members & filters.group)
async def grouup(client, message):
    botusername=await client.get_me()
    nyva=botusername.username
    user_id3= await db.is_bot_exist(nyva)
    if await is_user_exist(f"{user_id3}##{message.from_user.id}",nyva):
        return
    if await  is_subscribed(client, message, message.chat.id):
        hjkl = f'{user_id3}##{message.from_user.id}'
        if not await is_user_exist(hjkl,nyva):
            await add_user(hjkl,nyva)
    #await client.restrict_chat_member(message.chat.id, message.from_user.id,
        #ChatPermissions(can_send_messages=False)) 
    url=f"https://t.me/{nyva}?start=mwongozohrm{message.chat.id}"
    text=f"Karibu **{message.from_user.mention}**\n\nSamahani hutoweza kutuma chochote (Sababu ukituma nafuta) ,Ila tunapenda usome muongozo na jinsi ya kupakua huduma zetu ,Ndio tutakuruhusu kutuma ujumbe utakao penda.\n\n**[GUSA HAPA]({url})** kisha bonyeza  neno START ili kuweza kupata muongozo na maelekezo ya huduma zetu.."
    await message.reply_text(f"{text}")
@Bot0.on_message(filters.group & filters.incoming)
async def group(client, message):
    await handle_admin_status(client,message)
    botusername=await client.get_me()
    nyva=botusername.username
    user_id3= await db.is_bot_exist(nyva)
    gd=await db.get_db_status(int(user_id3))
    group_id = int(user_id3)
    hjkl = f'{user_id3}##{message.from_user.id}'
    if not await  is_subscribed(client, message, message.chat.id):
        await message.delete()
        gh=await is_user_exist(hjkl,nyva)
        if not gh:
            #await client.restrict_chat_member(message.chat.id, message.from_user.id,
                #ChatPermissions(can_send_messages=False)) 
            url=f"https://t.me/{nyva}?start=mwongozohrm{message.chat.id}"
            text=f"Ndugu **{message.from_user.mention}**\n\nSamahani hutoweza kutuma chochote **(Sababu ukituma nafuta)** ,Ila tunapenda usome muongozo na jinsi ya kupakua huduma zetu ,Ndio tutakuruhusu kutuma ujumbe utakao penda.\n\n**[GUSA HAPA]({url})** kisha bonyeza  neno START ili kuweza kupata muongozo na maelekezo ya huduma zetu.."
            await message.reply_text(f"{text}")
            return 
    
    if not message.text:
        return 
    try:
        hjkl = f'{user_id3}##{message.from_user.id}'
        if not await is_user_exist(hjkl,nyva):
            await add_user(hjkl,nyva)         
    except :
        pass
    user_id4 = gd['user_link']
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        searchi = message.text.lower()
        files = await get_filter_results(searchi,user_id3)
        if len(files)==1:
            for document in files:
                id3 = document.id
                reply_text = document.reply
                button = document.btn
                alert = document.price
                file_status = document.grp
                fileid = document.file
                keyword = document.text.split('.dd#.',1)[0]
                msg_type = document.type
                descp = document.descp.split('.dd#.')[1]
                acs = document.descp.split('.dd#.')[0]
                if button =="[]":
                    reply_markup = None
                else:
                    reply_markup = InlineKeyboardMarkup(eval(button))
                if reply_text:
                    reply_text = reply_text.replace("\\n", "\n").replace("\\t", "\t")
                if acs == 'x':  
                    if fileid == 'None':
                        await message.reply_text(text=f'{reply_text}',reply_markup = reply_markup)
               
                    elif msg_type == 'Photo' and file_status != 'normal':
                        await message.reply_photo(
                            photo = fileid,
                            caption = reply_text+'\nBonyeza **DOWNLOAD** kuipakua',
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('📤 Download', url=f"https://t.me/{nyva}?start=subinps_-_-_-_{id3}")]])if group_id != message.from_user.id else InlineKeyboardMarkup([[InlineKeyboardButton('📤 Download', url=f"https://t.me/{nyva}?start=subinps_-_-_-_{id3}")],[InlineKeyboardButton(' Edit', url=f"https://t.me/{nyva}?start=xsubinps_-_-_-_{id3}")]])
                        )
                 
                    elif msg_type == 'Photo':
                        await message.reply_photo(
                            photo = fileid,
                            caption = reply_text or '',
                            reply_markup=reply_markup
                        )
                
                    elif fileid and file_status != 'normal':
                        await message.reply_cached_media(
                            file_id = fileid,
                            caption = reply_text+'\nBonyeza **DOWNLOAD** kuipakua' or "",
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('📤 Download', url=f"https://t.me/{nyva}?start=subinps_-_-_-_{id3}")]])if group_id != message.from_user.id else InlineKeyboardMarkup([[InlineKeyboardButton('📤 Download', url=f"https://t.me/{nyva}?start=subinps_-_-_-_{id3}")],[InlineKeyboardButton(' Edit', url=f"https://t.me/{nyva}?start=xsubinps_-_-_-_{id3}")]])
                        )
                
                    elif fileid:
                        await message.reply_cached_media(
                            file_id = fileid,
                            caption = reply_text or "",
                            reply_markup=reply_markup
                        )  
        elif files:
            await message.reply_text(f"<b>Bonyeza kitufe <b>(🔍 Majibu ya Database : {len(files)})</b> Kisha chagua unachokipenda kwa kushusha chini\n\n💥Kwa urahisi zaidi kutafta chochote anza na aina kama ni  movie, series ,(audio ,video) kwa music , vichekesho kisha acha nafasi tuma jina la  kitu unachotaka mfano video jeje au audio jeje au movie extraction au series soz­</b>", reply_markup=get_reply_makup(searchi,len(files)))
        elif searchi.startswith('movie') or searchi.startswith('series') or searchi.startswith('dj'):
            await message.reply_text(text=f'Samahani **{searchi}** uliyotafta haipo kwenye database zetu.\n\nTafadhali bonyeza Button kisha ukurasa unaofuata ntumie jina la movie au series ntakupa jibu kwa haraka iwezekanavyo ili nii tafte',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='ADMIN',url=f'{user_id4}')]]))
            return
        else:
            return
        if not btn:
            return
            
@Bot0.on_message(filters.regex('@gmail.com') & filters.incoming)
async def groupprv(client, message): 
    botusername=await client.get_me()
    nyva=botusername.username
    user_id3= await db.is_bot_exist(nyva)
    gd=await db.get_db_status(int(user_id3))
    group_id = int(user_id3)
    hjkl = f'{user_id3}##{message.from_user.id}'
    text=message.text
    if " " not in text.strip() and "@gmail.com" in text.lower():
        group_status = await is_user_exist(hjkl,nyva)
        user_id3='hrm45'
        if group_status:
            for user in group_status:
                user_id3 = user.email
            text1='TAFADHALI MPE ACCESS YA MOVIE/VIFURUSHI HIVI'
            async for dtls in await db.get_acc(message.from_user.id ):
                if dtls["user_id"] == message.from_user.id:
                    if dtls["file_id"].startswith("g_") and dtls["db_name"]==group_id:
                        text1+=f"gh\n"
                    else:
                        text1+='gh\n'
            if user_id3 == text.lower():
                await message.reply_text('Hii email tayar Tulishaihifadhi kama unataka kuibadisha ntumie nyingene')
            elif text1!='TAFADHALI MPE ACCESS YA MOVIE/VIFURUSHI HIVI\n':
                await message.reply_text('Tumeibadilisha kikamilifu')
                await User.collection.update_one({'_id':message.from_user.id},{'$set':{'email':text.lower()}})
                if await db.is_email_exist(message.from_user.id):
                    await message.reply_text(f'Tafadhali subir kidogo tutakupa taarifa tutakaipo iwezesha')
                    await client.send_message(chat_id=group_id,text=f'Tafadhal iwezeshe email hii **{message.text.strip()}** \n kisha ondoa uwezo kwenye email hii **{user_id3}** Kisha baada ya kumaliza kumuwekea access bonyeza done..\n{text1}done',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Done', callback_data =f'done {message.from_user.id}')]]))
            else:
                await message.reply_text('Tafadhali hujajiunga na kifurushi chochote cha kwetu jiunge kwanza ndio tutawezesha email yako')
        else:
            await message.reply_text(f'Tafadhali jiunge kwanza na kikund chetu {gd["group"].split("##")[1]}\nkisha ndio tutaadd email yako')         
    else:
        await message.reply_text('Tafadhal ujumbe huu uliontumia sjauelewa Tafadhali kama n email:ntumie email tu bila neno jingine \nMfano  mohamed@gmail.com \n\nZingatia\n1.usiruke nafasi kwenye email yako  \n2.hakisha n gmail (hrmr5@gmail.com)\n3.hakikisha huongez neno lingine zaid ya email \n\nKwa salio lako tuma neno Salio \nZingatia lianze na herufi kubwa S na hizo nyingine ndogo\n\n Maelekezo mengine mchek hrm45')
        return
def get_reply_makup(query,totol):
    buttons = [
        [
            InlineKeyboardButton('🔍Majibu ya Database: '+ str(totol), switch_inline_query_current_chat=query),
        ]
        ]
    return InlineKeyboardMarkup(buttons)
