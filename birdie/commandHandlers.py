from ast import Call
import os
import subprocess
import logging
import traceback, html, json

from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from helper import admin_only
from models import *

DEVELOPER_CHAT_ID = 1262447783

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def add_venue(update: Update, context: CallbackContext) -> None:
    message = update.message or update.edited_message
    channel = TgChannel.find_or_create(update.effective_chat.id)
    if message.reply_to_message and message.reply_to_message.text:
        venue_data = message.reply_to_message.text.split(':')
        if len(venue_data) == 6:
            venue = Venue.find_or_create(venue_data[0])
            venue.channel = channel
            venue.address = venue_data[1]
            venue.suburb = venue_data[2]
            venue.phone = venue_data[3]
            venue.map_url = venue_data[4]
            venue.courts = int(venue_data[5])
            venue.save()
            update.message.reply_text(f"Venue {venue.name} has been added to this channel.")
            return
    update.message.reply_text("Venue format: \"name:address:subrub:phone:map_url:courts\"")

def list_venues(update: Update, context: CallbackContext) -> None:
    channel = TgChannel.find_or_create(update.effective_chat.id)
    venues = Venue.list(channel)
    update.message.reply_text(
        "Showing venues:\n" +
        "\n".join([v.name for v in venues])
    )

def error_handler(update: Update, context: CallbackContext) -> None:
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    # You might need to add some logic to deal with messages longer than the 4096 character limit.
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html.escape(str(context.chat_data))}</pre>\n\n"
        f"<pre>context.user_data = {html.escape(str(context.user_data))}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    # Finally, send the message
    context.bot.send_message(
        chat_id=DEVELOPER_CHAT_ID, text=message, parse_mode=ParseMode.HTML
    )
    update.message.reply_text("Oops something messed up here. My master has been notified.")
