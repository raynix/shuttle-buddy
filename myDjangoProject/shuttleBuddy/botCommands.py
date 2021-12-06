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
    game = SocialGame.find_game(game_message.text)
    if game is None:
        update.message.reply_text("lease reply '/book' to the message which has the game you wanted to book.")
        return

    update.message.reply_text(f'{game_message.text} has been booked.')
    print(game_message)
