from telegram import ChatAction, Update, InlineKeyboardButton, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from consts import HELP_MSG, STOP_MSG, UNKNOWN_MSG, START_MSG, Gui, GUI
from utiles import send_action, bt_menu, key_menu


@send_action(ChatAction.TYPING)
def start(update: Update, context: CallbackContext) -> None:
    if Gui == GUI.key:
        key_start(update, context)
    elif Gui == GUI.button:
        bt_start(update, context)


@send_action(ChatAction.TYPING)
def stop(update: Update, context: CallbackContext) -> None:
    key_stop(update, context)


@send_action(ChatAction.TYPING)
def help(update: Update, context: CallbackContext) -> None:
    if Gui == GUI.key:
        key_help(update, context)
    elif Gui == GUI.button:
        bt_help(update, context)


def key_start(update: Update, context: CallbackContext) -> None:
    keyboard_list = [['gallery', 'order'],
                       ['help', 'stop']]
    key_menu(update, context, keyboard_list, START_MSG)


def bt_start(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, START_MSG)


def key_stop(update: Update, context: CallbackContext) -> None:
    # keyboard_list = [['start']]
    # key_menu(update, context, keyboard_list, STOP_MSG)
    reply_markup = ReplyKeyboardRemove()
    context.bot.send_message(chat_id=update.effective_chat.id, text=STOP_MSG, reply_markup=reply_markup)
    bt_stop(update, context)


def bt_stop(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("start", callback_data='bt_start')
    ]
    bt_menu(update, context, button_list, STOP_MSG, 1)


def key_help(update: Update, context: CallbackContext) -> None:
    keyboard_list = [['gallery', 'order'],
                       ['stop']]
    key_menu(update, context, keyboard_list, HELP_MSG)


def bt_help(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("gallery", callback_data='bt_gallery'),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, HELP_MSG)


# @send_action(ChatAction.TYPING)
# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')


# @send_action(ChatAction.TYPING)
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# @send_action(ChatAction.TYPING)
# def caps(update, context):
#     if len(context) == 0:
#         return
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
# dispatcher.add_handler(CommandHandler('caps', caps))
# dispatcher.add_handler(CommandHandler('stop', stop_prog))

# def stop_prog(update, context):
# 	context.bot.send_message(chat_id=update.effective_chat.id, text=STOP_MSG)
# 	updater.stop()


@send_action(ChatAction.TYPING)
def add_group(update: Update, context: CallbackContext) -> None:
    for member in update.message.new_chat_members:
        update.message.reply_text(f"{member.full_name} just joined the group")
        update.message.reply_text(START_MSG)


@send_action(ChatAction.TYPING)
def unknown(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text=UNKNOWN_MSG)
