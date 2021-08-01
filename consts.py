import enum

STOP_MSG = 'Stoping the bot... use /start to start again'
START_MSG = 'Welcome to Michael\'s meat shop, use /help to get access to the commands'
HELP_MSG = '/gallery to see the meat\n/order to begin your order'
GALLERY_MSG = 'use /order to begin your order'
ORDER_MSG = 'choose a category'
ORDER_BEEF_MSG = 'beef types:'
ORDER_CHICKEN_MSG = 'chicken types:'
UNKNOWN_MSG = 'Sorry, I didn\'t understand that command\nuse /help to see what commands you can use'


class Gui(enum.Enum):
    key = 0
    button = 1


GUI = Gui.key
