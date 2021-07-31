from typing import List

from telegram import ChatAction, Update, InputMediaDocument, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from consts import HELP_MSG, STOP_MSG, GALLERY_MSG, UNKNOWN_MSG, START_MSG
from utiles import send_action, build_menu

media_1 = InputMediaDocument(media=open('data/img1.jpg', 'rb'))
media_2 = InputMediaDocument(media=open('data/img2.jpg', 'rb'))
media_3 = InputMediaDocument(media=open('data/img3.jpg', 'rb'))
media_4 = InputMediaDocument(media=open('data/img4.jpg', 'rb'))
media_5 = InputMediaDocument(media=open('data/img5.jpg', 'rb'))
media_6 = InputMediaDocument(media=open('data/img6.jpg', 'rb'))

CHICKEN = [media_1, media_2]
BEEF = [media_3, media_4, media_5, media_6]
ALL_MEAT = [media_1, media_2, media_3, media_4, media_5, media_6]


@send_action(ChatAction.TYPING)
def bt_menu(update: Update, context: CallbackContext, button_list: List, n_cols: int = 2) -> InlineKeyboardMarkup:
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=n_cols))
    return reply_markup


@send_action(ChatAction.TYPING)
def bt_start(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list)
    context.bot.send_message(chat_id=update.effective_chat.id, text=START_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def bt_help(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("gallery", callback_data='bt_gallery'),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list)
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def bt_stop(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("start", callback_data='bt_start')
    ]
    reply_markup = bt_menu(update, context, button_list, 1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=STOP_MSG, reply_markup=reply_markup)


@send_action(ChatAction.UPLOAD_PHOTO)
def bt_gallery_chicken(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 1)
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=CHICKEN)
    context.bot.send_message(chat_id=update.effective_chat.id, text=GALLERY_MSG, reply_markup=reply_markup)


@send_action(ChatAction.UPLOAD_PHOTO)
def bt_gallery_beef(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 1)
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=BEEF)
    context.bot.send_message(chat_id=update.effective_chat.id, text=GALLERY_MSG, reply_markup=reply_markup)


@send_action(ChatAction.UPLOAD_PHOTO)
def bt_gallery_all(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 1)
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=ALL_MEAT)
    context.bot.send_message(chat_id=update.effective_chat.id, text=GALLERY_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def bt_gallery(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("all types", callback_data="gallery_all"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("beef", callback_data="gallery_beef"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("chicken", callback_data="gallery_chicken"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=GALLERY_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def start(update: Update, context: CallbackContext) -> None:
    bt_start(update, context)


@send_action(ChatAction.TYPING)
def help(update: Update, context: CallbackContext) -> None:
    bt_help(update, context)


@send_action(ChatAction.UPLOAD_PHOTO)
def gallery(update: Update, context: CallbackContext) -> None:
    bt_gallery(update, context)


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
