import os
import json
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ParseMode
import moralis

tg_token = os.environ.get('TG_BOT_API_KEY')

# Initialize the Telegram bot, updater, and dispatcher
updater = Updater(tg_token)
bot = updater.bot
dispatcher = updater.dispatcher

def start(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        message = body.get('message', {})
        chat_id = message.get('chat', {}).get('id')
        print("this is chat_id", chat_id)

        message_text = "*----text-----*"

        # Assuming moralis.get_prices() can potentially raise an exception
        crypto_data = moralis.get_prices()

        for entry in crypto_data:
            TokenName = entry["tokenName"]
            TokenPrice = entry["usdPrice"]
            TokenAddress = entry["tokenAddress"]
            Token_24change_hour = entry["24hrPercentChange"]
            
            TokenPrice = float(TokenPrice)
            Token_24change_hour = float(Token_24change_hour)

            message_text += f"\n\nToken Name: {TokenName}\nToken Price: ${TokenPrice:,.6f}\n24Hour Change: {Token_24change_hour:.3f}%\nToken Address: {TokenAddress}\n"
            print("capture the token entry", entry)

        bot.send_message(chat_id=chat_id, text=message_text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        # Handle exceptions here
        print(f"An unexpected error occurred: {e}")
        # Optionally, you can send an error message to the user
        bot.send_message(chat_id=chat_id, text="An unexpected error occurred while processing your request.")

# Register the command handler
dispatcher.add_handler(CommandHandler("start", start))
