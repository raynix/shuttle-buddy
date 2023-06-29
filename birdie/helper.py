
def admin_only(func):
    def wrapper(*args, **kwargs):
        if 'update' in kwargs:
            update = kwargs['update']
            member = update.effective_chat.get_member(update.message.from_user.id)
            if member.status and member.status in ['administrator', 'creator']:
                return func(*args, **kwargs)
    return wrapper
