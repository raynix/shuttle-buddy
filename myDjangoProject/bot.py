import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PollHandler, PollAnswerHandler, RegexHandler, CallbackContext
from telegram import Update

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shuttleBuddy.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from shuttleBuddy.botCommands import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Inform user about what this bot can do"""
    update.message.reply_text(
        'Please select one of the following options:\n'
        '/venue show available venues\n'
    )

def debug(update: Update, context: CallbackContext) -> None:
    """Debugging function"""
    print(update)
    print(context)


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.environ["BOT_TOKEN"])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('venue', venue))
    # dispatcher.add_handler(PollAnswerHandler(receive_poll_answer))
    dispatcher.add_handler(CommandHandler('game', social_game))
    # dispatcher.add_handler(PollHandler(receive_quiz_answer))
    dispatcher.add_handler(CommandHandler('book', book_game))
    dispatcher.add_handler(MessageHandler(Filters.all, debug))
    # dispatcher.add_handler(CommandHandler('help', help_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()