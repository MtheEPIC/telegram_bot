import os
from functools import wraps
from typing import List, Union
from uuid import uuid4

from telegram import InlineKeyboardButton, ChatAction, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

KEY_LENGTH = 46


def get_key() -> str:
    key_file = os.open('key.txt', os.O_RDONLY)
    key = os.read(key_file, KEY_LENGTH)
    os.close(key_file)
    return key.decode()


def send_action(action: ChatAction):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context, *args, **kwargs)

        return command_func

    return decorator


def build_menu(
        buttons: List[InlineKeyboardButton],
        n_cols: int,
        header_buttons: Union[InlineKeyboardButton, List[InlineKeyboardButton]] = None,
        footer_buttons: Union[InlineKeyboardButton, List[InlineKeyboardButton]] = None
) -> List[List[InlineKeyboardButton]]:
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons if isinstance(header_buttons, list) else [header_buttons])
    if footer_buttons:
        menu.append(footer_buttons if isinstance(footer_buttons, list) else [footer_buttons])
    return menu


def bt_menu(update: Update, context: CallbackContext, button_list: List[InlineKeyboardButton],
            text: str = 'Custom Buttons', n_cols: int = 2) -> None:
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=n_cols))
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)


def key_menu(update: Update, context: CallbackContext, keyboard_list: List[List[str]],
             text: str = 'Custom Keyboard') -> None:
    reply_markup = ReplyKeyboardMarkup(keyboard_list)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)


def put(update: Update, context: CallbackContext, key: str, value: int) -> None:
    user = update.effective_chat.id
    old_value = get(update, context, key)
    if value == 1:
        old_value += 1
    elif value == -1:
        old_value -= 1 if old_value > 0 else 0
    else:
        raise ValueError("value must be +1 or -1")
    context.user_data[user].update({key: old_value})


def get(update: Update, context: CallbackContext, key: str) -> int:
    user = update.effective_chat.id
    try:
        context.user_data[user]
    except KeyError:
        context.user_data.update({user: dict()})
    try:
        value = context.user_data[user][key]
    except KeyError:
        value = 0
        context.user_data[user].update({key: value})
    return value
