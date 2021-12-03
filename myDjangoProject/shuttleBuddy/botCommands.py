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
