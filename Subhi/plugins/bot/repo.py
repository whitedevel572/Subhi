from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Subhi import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє ƒσя SUBHI яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝐌𝐔𝐉𝐇𝐄 𝐋𝐄 𝐂𝐇𝐀𝐋𝐎 𝐘𝐑𝐑🥺", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/SUBI_WORLD"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/SUBHI_LOVE"),
          ],
               [
                InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url=f"https://t.me/SUBI_WORLD"),

],
[
              InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://github.com/Subhichiku/SubhiBANALL"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/Subhichiku/Subhi"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://github.com/Subhichiku/Subhi-Management"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/subhichiku/Chiku-chat"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://github.com/Subhichiku/SubhiSTRING"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://github.com/Subhichiku/chiku-chat"),
],
[
              InlineKeyboardButton("𝗩𝗣𝗦", url=f"https://github.com/subhichiku/Kaali-Linux"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://github.com/subhichiku/"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://github.com/subhichiku/"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://github.com/subhichiku/"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://github.com/subhichiku/"),
InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛𝗕𝗢𝗧", url=f"https://github.com/subhichiku/"),
],
[
InlineKeyboardButton("𝗖𝗖 𝗕𝗢𝗧", url=f"https://github.com/subhichiku/"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/f73f8ab100aa73b3286f5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
