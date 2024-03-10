from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from EsproMusic import app
from config import BOT_USERNAME
from EsproMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωєℓ¢σмє тσ тєαм єѕρяσ яєρσ ✪
 
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
          InlineKeyboardButton("Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("🍁Sᴜᴘᴘᴏʀᴛ🥀", url="https://t.me/EsproSupport"),
          InlineKeyboardButton("🍁Uᴘᴅᴀᴛᴇ🥀", url="https://t.me/EsproUpdate"),
          ],
               [
                InlineKeyboardButton("❄️Oᴡɴᴇʀ❄️", url="https://t.me/i_ii_ritikraj_ii_i"),

],
[
              InlineKeyboardButton("—͟͞͞★Mᴜꜱɪᴄㅤ✓︎", url=f"https://github.com/TeamEspro/EsproMusicBot"),
              InlineKeyboardButton("︎—͟͞͞★Sᴛʀɪɴɢㅤ✓", url=f"https://github.com/TeamEspro/EsproStringBot"),
              ],
              [
                InlineKeyboardButton("● ◀️───ᴄʜᴀᴛ────▶ ●", url="https://github.com/TeamEspro/EsproChatBot"),
                ]]
              
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/de9e5afa186bbe69e7c0c.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/TeamEspro/EsproAiMusicBot/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[🍁Sᴜᴘᴘᴏʀᴛ🥀](https://t.me/EsproSupport) | [🍁Uᴘᴅᴀᴛᴇ🥀](https://t.me/EsproUpdate)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")

