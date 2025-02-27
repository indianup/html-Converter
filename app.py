from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from core import handle_file, start
from logs import setup_logger

# Set up logging
logger = setup_logger()

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, handle_file))

    # Start the bot
    logger.info("Starting the bot...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
