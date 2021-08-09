from telegram import Update, ChatAction
from telegram.ext import CallbackContext

from consts import ADMIN
from utiles import get_all, send_action


@send_action(ChatAction.TYPING)
def pay(update: Update, context: CallbackContext) -> None:
    ordered_items = get_all(update, context)
    context.bot.send_message(chat_id=ADMIN, text='user: {}|{} order: {}'
                             .format(update.effective_user.full_name, update.effective_user.username, str(ordered_items)))
    context.bot.send_message(chat_id=update.effective_chat.id, text='sent order to admin')
