import os
import re
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ['BOT_TOKEN']
TARGET_CHANNEL = 'https://t.me/lebasomdekhoadam'  # آیدی کانال مقصدتو اینجا بذار

def remove_emojis(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
        u"\u2600-\u26FF"
        u"\u2700-\u27BF"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def rewrite_caption(caption):
    lines = remove_emojis(caption).splitlines()
    result = []

    for line in lines:
        l = line.strip()
        if not l:
            continue
        if 'مدل' in l:
            result.append(f"🔰 {l} 🔰")
        elif 'پارچه' in l:
            result.append(f"❇️ {l} ❇️")
        elif 'سایز' in l:
            result.append(f"❇️ {l} ❇️")
        elif 'پک' in l:
            result.append(f"❇️ {l} ❇️")
        elif 'تضمین' in l:
            result.append(f"❇️ {l} ❇️")
        elif 'قیمت' in l:
            result.append(f"✅ {l} ✅")

    result.append("\n⬇️ جهت سفارش ⬇️")
    result.append("@Mr_nouri00")
    result.append("09399300342")

    return '\n\n'.join(result)

async def handle_channel_post(update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if post and post.photo:
        original_caption = post.caption or ""
        modified_caption = rewrite_caption(original_caption)
        await context.bot.send_photo(
            chat_id=TARGET_CHANNEL,
            photo=post.photo[-1].file_id,
            caption=modified_caption
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.Channel(), handle_channel_post))

print("✅ Bot is running...")
app.run_polling()
