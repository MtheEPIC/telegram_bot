from telegram import ChatAction, Update, InlineKeyboardButton, InputMediaDocument
from telegram.ext import CallbackContext

from consts import GALLERY_MSG
from utiles import send_action, bt_menu, key_menu

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
def gallery(update: Update, context: CallbackContext) -> None:
    key_gallery(update, context)


def key_gallery(update: Update, context: CallbackContext) -> None:
    keyboard_list = [['all types', 'beef', 'chicken'],
                       ['help', 'order', 'stop']]
    key_menu(update, context, keyboard_list, GALLERY_MSG)


def bt_gallery(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("all types", callback_data="gallery_all"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("beef", callback_data="gallery_beef"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("chicken", callback_data="gallery_chicken"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, GALLERY_MSG, 2)


@send_action(ChatAction.UPLOAD_PHOTO)
def bt_gallery_chicken(update: Update, context: CallbackContext) -> None:
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=CHICKEN)
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, GALLERY_MSG, 1)


@send_action(ChatAction.UPLOAD_PHOTO)
def bt_gallery_beef(update: Update, context: CallbackContext) -> None:
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=BEEF)
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, GALLERY_MSG, 1)


@send_action(ChatAction.UPLOAD_PHOTO)
def bt_gallery_all(update: Update, context: CallbackContext) -> None:
    context.bot.send_media_group(chat_id=update.effective_chat.id, media=ALL_MEAT)
    button_list = [
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, GALLERY_MSG, 1)
