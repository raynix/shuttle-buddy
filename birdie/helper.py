from telegram.constants import CHATMEMBER_ADMINISTRATOR, CHATMEMBER_CREATOR
def admin_only(func):
    def wrapper(*args, **kwargs):
        # all handler function has Update as the first argument
        update = args[0]
        # https://docs.python-telegram-bot.org/en/stable/telegram.chat.html#telegram.Chat.get_member
        member = update.effective_chat.get_member(update.message.from_user.id)
        if member.status and member.status in [CHATMEMBER_ADMINISTRATOR, CHATMEMBER_CREATOR]:
            return func(*args, **kwargs)
        else:
            update.message.reply_text("This command is for group admin only.")
    return wrapper
