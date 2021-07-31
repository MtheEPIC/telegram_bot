from telegram import InlineKeyboardButton, ChatAction, Update
from telegram.ext import CallbackContext

from consts import ORDER_MSG, ORDER_CHICKEN_MSG, ORDER_BEEF_MSG
from funcs import bt_menu
from utiles import send_action

breasts = 0
chicks = 0


@send_action(ChatAction.TYPING)
def order(update: Update, context: CallbackContext) -> None:
    bt_order(update, context)


@send_action(ChatAction.TYPING)
def bt_order(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("beef", callback_data="order_beef"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicken", callback_data="order_chicken"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ORDER_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def bt_order_beef(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("beef", callback_data="bt_order_beef"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicken", callback_data="bt_order_chicken"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ORDER_BEEF_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def bt_order_chicken(update: Update, context: CallbackContext) -> None:
    button_list = [
            InlineKeyboardButton("breasts", callback_data="order_breasts"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicks", callback_data="order_chicks"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ORDER_CHICKEN_MSG, reply_markup=reply_markup)


@send_action(ChatAction.TYPING)
def bt_order_chicks(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("+", callback_data="chicks_plus"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("-", callback_data="chicks_minus"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"number of chicks: {chicks}", reply_markup=reply_markup)


def chicks_plus(update: Update, context: CallbackContext) -> None:
    global chicks
    chicks += 1
    bt_order_chicks(update, context)


def chicks_minus(update: Update, context: CallbackContext) -> None:
    global chicks
    chicks -= 1 if chicks > 0 else 0
    bt_order_chicks(update, context)


@send_action(ChatAction.TYPING)
def bt_order_breasts(update: Update, context: CallbackContext) -> None:
    button_list = [
        InlineKeyboardButton("breasts", callback_data="order_breasts"),
        InlineKeyboardButton("help", callback_data='bt_help'),
        InlineKeyboardButton("chicks", callback_data="order_chicks"),
        InlineKeyboardButton("order", callback_data="bt_order"),
        InlineKeyboardButton("stop", callback_data="bt_stop")
    ]
    reply_markup = bt_menu(update, context, button_list, 2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ORDER_CHICKEN_MSG, reply_markup=reply_markup)
