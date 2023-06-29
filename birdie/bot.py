import os
import logging
import mongoengine
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
from commandHandlers import *

TOKEN = os.environ["BOT_TOKEN"]
PROD = os.environ.get("PROD", "false")
DOMAIN = os.environ.get("DOMAIN", "luckybirdie.awes.one")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

mongoengine.connect(
    db=os.environ['MONGODB_DB'],
    host=os.environ['MONGODB_HOST'],
    username=os.environ['MONGODB_USERNAME'],
    password=os.environ['MONGODB_PASSWORD']
)

def help(update: Update, context: CallbackContext) -> None:
    """Inform user about what this bot can do"""
    update.message.reply_text(
        'Hello, world!'
    )

def debug(update: Update, context: CallbackContext) -> None:
    """Debugging function"""
    logger.info(update)
    logger.info(context)


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('debug', debug))
    # dispatcher.add_handler(CommandHandler('users', users))
    # dispatcher.add_handler(CommandHandler('adduser', add_user))

    dispatcher.add_error_handler(error_handler, run_async=True)

    # Start the Bot
    if PROD == 'true':
    # enable webhook
        updater.start_webhook(listen="0.0.0.0", port=8000, url_path=TOKEN, webhook_url=f'https://{DOMAIN}/{TOKEN}')
    else:
        # enable polling
        updater.start_polling()
    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
