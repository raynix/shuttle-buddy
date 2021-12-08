import os

from shuttleBuddy.models import *

from telegram import Update
from telegram.ext import CallbackContext

def venue(update: Update, context: CallbackContext) -> None:
    venues = Venue.objects.all()
    if len(venues) == 0:
        update.message.reply_text("No venues have been added yet.")
    else:
        update.message.reply_text(
            'Available venues:\n'
            + '\n'.join(f'{venue.name} - {venue.address}' for venue in venues)
        )

def social_game(update: Update, context: CallbackContext) -> None:
    games = SocialGame.objects.all()
    if len(games) == 0:
        update.message.reply_text("No social games have been added yet.")
    else:
        update.message.reply_text('Available social games:\n')
        for game in games:
            update.message.reply_text(f"{game}")

def book_game(update: Update, context: CallbackContext) -> None:
    game_message = update.effective_message.reply_to_message
    error_message = "Please reply '/book' to the message which has the game you wanted to book. Use '/game' to show available games."
    if game_message is None:
        update.message.reply_text(error_message)
        return

    game = SocialGame.find_game(game_message.text)
    if game is None:
        update.message.reply_text(error_message)
        return

    player = Player.find_or_create(update.effective_user.username)
    booking, message = Booking.find_or_create(player, game)

    update.message.reply_text(message)


"""
{
    'new_chat_photo': [],
    'text': 'Test Game on 2018-01-01 at 12:00:00',
    'photo': [],
    'new_chat_members': [],
    'date': 1638750720,
    'supergroup_chat_created': False,
    'group_chat_created': False,
    'entities': [],
    'caption_entities': [],
    'message_id': 38,
    'delete_chat_photo': False,
    'channel_chat_created': False,
    'chat': {
        'type': 'private',
        'id': 1262447783,
        'username': 'raynix1',
        'first_name': 'raynix'
    },
    'from': {
        'is_bot': True,
        'id': 2119089823,
        'username': 'shuttle_buddy_bot',
        'first_name': 'shuttle-buddy'
    }
}
"""