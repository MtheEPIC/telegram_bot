from telegram import InlineKeyboardButton, ChatAction, Update
from telegram.ext import CallbackContext

from consts import ORDER_MSG, ORDER_CHICKEN_MSG, ORDER_BEEF_MSG, Gui, GUI, order_keyboard_list
from utiles import send_action, bt_menu, key_menu, get

entrecote = 0
butcher_cut = 0
chicks = 0
breasts = 0


@send_action(ChatAction.TYPING)
def order(update: Update, context: CallbackContext) -> None:
    if Gui == GUI.key:
        key_order(update, context)
    elif Gui == GUI.button:
        bt_order(update, context)


@send_action(ChatAction.UPLOAD_PHOTO)
def order_beef(update: Update, context: CallbackContext) -> None:
    if Gui == GUI.key:
        key_order_beef(update, context)
    elif Gui == GUI.button:
        bt_order_beef(update, context)


@send_action(ChatAction.UPLOAD_PHOTO)
def order_chicken(update: Update, context: CallbackContext) -> None:
    if Gui == GUI.key:
        key_order_chicken(update, context)
    elif Gui == GUI.button:
        bt_order_chicken(update, context)


def order_product(update: Update, context: CallbackContext, product: str):
    if product == 'entrecote':
        order_entrecote(update, context)
    elif product == 'butcher cut':
        order_butcher_cut(update, context)
    elif product == 'chicks':
        order_chicks(update, context)
    elif product == 'breasts':
        order_breasts(update, context)
    else:
        raise ValueError("product must be one of the available options")


@send_action(ChatAction.TYPING)
def order_entrecote(update: Update, context: CallbackContext) -> None:
    global entrecote
    entrecote = get(update, context, 'entrecote')
    if Gui == GUI.key:
        key_order_entrecote(update, context)
    elif Gui == GUI.button:
        bt_order_entrecote(update, context)


@send_action(ChatAction.TYPING)
def order_butcher_cut(update: Update, context: CallbackContext) -> None:
    global butcher_cut
    butcher_cut = get(update, context, 'butcher cut')
    if Gui == GUI.key:
        key_order_butcher_cut(update, context)
    elif Gui == GUI.button:
        bt_order_butcher_cut(update, context)


@send_action(ChatAction.TYPING)
def order_chicks(update: Update, context: CallbackContext) -> None:
    global chicks
    chicks = get(update, context, 'chicks')
    if Gui == GUI.key:
        key_order_chicks(update, context)
    elif Gui == GUI.button:
        bt_order_chicks(update, context)


@send_action(ChatAction.TYPING)
def order_breasts(update: Update, context: CallbackContext) -> None:
    global breasts
    breasts = get(update, context, 'breasts')
    if Gui == GUI.key:
        key_order_breasts(update, context)
    elif Gui == GUI.button:
        bt_order_breasts(update, context)


def key_order(update: Update, context: CallbackContext) -> None:
    keyboard_list = [['beef', 'chicken'],
                     ['gallery', 'help', 'stop']]
    key_menu(update, context, keyboard_list, ORDER_MSG)


def bt_order(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("beef", callback_data="order_beef"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicken", callback_data="order_chicken"),
        InlineKeyboardButton("gallery", callback_data="bt_gallery"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, ORDER_MSG, 2)


def key_order_beef(update: Update, context: CallbackContext) -> None:
    keyboard_list = [['entrecote', 'butcher cut', 'order'],
                     ['gallery', 'help', 'stop']]
    key_menu(update, context, keyboard_list, ORDER_BEEF_MSG)


def bt_order_beef(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("entrecote", callback_data="order_entrecote"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("butcher cut", callback_data="order_butcher_cut"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, ORDER_BEEF_MSG, 2)


def key_order_chicken(update: Update, context: CallbackContext) -> None:
    keyboard_list = [['breasts', 'chicks', 'order'],
                     ['help', 'stop']]
    key_menu(update, context, keyboard_list, ORDER_CHICKEN_MSG)


def bt_order_chicken(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("breasts", callback_data="order_breasts"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicks", callback_data="order_chicks"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, ORDER_CHICKEN_MSG, 2)


def key_order_entrecote(update: Update, context: CallbackContext) -> None:
    key_menu(update, context, order_keyboard_list, f"number of entrecote: {entrecote}")


def key_order_butcher_cut(update: Update, context: CallbackContext) -> None:
    key_menu(update, context, order_keyboard_list, f"number of butcher cut: {butcher_cut}")


def key_order_chicks(update: Update, context: CallbackContext) -> None:
    key_menu(update, context, order_keyboard_list, f"number of chicks: {chicks}")


def key_order_breasts(update: Update, context: CallbackContext) -> None:
    key_menu(update, context, order_keyboard_list, f"number of breasts: {breasts}")


def bt_order_chicks(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("+", callback_data="chicks_plus"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("-", callback_data="chicks_minus"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, f"number of chicks: {chicks}", 2)


# def key_order_breasts(update: Update, context: CallbackContext) -> None:
#     keyboard_list = [['breasts', 'order', 'temp'],
#                      ['help', 'stop']]
#     key_menu(update, context, keyboard_list, ORDER_CHICKEN_MSG)


def bt_order_breasts(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("breasts", callback_data="order_breasts"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicks", callback_data="order_chicks"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    bt_menu(update, context, button_list, ORDER_CHICKEN_MSG, 2)
