from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

from funcs import start, help, add_group, unknown, stop
from order import order, chicks_plus, chicks_minus, order_beef, order_chicken, order_chicks, order_breasts
from gallery import gallery, gallery_all, gallery_beef, gallery_chicken
from utiles import get_key


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(get_key())
dispatcher = updater.dispatcher

previous = None


def selector(update, context):
    global previous
    if update.message.text == 'stop':
        stop(update, context)
    elif update.message.text == 'start':
        start(update, context)
    elif update.message.text == 'help':
        help(update, context)
    elif update.message.text == 'gallery':
        gallery(update, context)
    elif update.message.text == 'order':
        order(update, context)

    elif update.message.text == 'all types':
        gallery_all(update, context)
    elif update.message.text == 'beef':
        if previous == 'gallery':
            gallery_beef(update, context)
        elif previous == 'order':
            order_beef(update, context)

    previous = update.message.text


dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, add_group))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('stop', stop))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('gallery', gallery))
dispatcher.add_handler(CommandHandler('order', order))

dispatcher.add_handler(CallbackQueryHandler(start, pattern="bt_start"))
dispatcher.add_handler(CallbackQueryHandler(stop, pattern="bt_stop"))
dispatcher.add_handler(CallbackQueryHandler(help, pattern="bt_help"))

dispatcher.add_handler(CallbackQueryHandler(gallery, pattern="bt_gallery"))
dispatcher.add_handler(CallbackQueryHandler(gallery_all, pattern="gallery_all"))
dispatcher.add_handler(CallbackQueryHandler(gallery_beef, pattern="gallery_beef"))
dispatcher.add_handler(CallbackQueryHandler(gallery_chicken, pattern="gallery_chicken"))

dispatcher.add_handler(CallbackQueryHandler(order, pattern="bt_order"))
dispatcher.add_handler(CallbackQueryHandler(order_beef, pattern="order_beef"))
dispatcher.add_handler(CallbackQueryHandler(order_chicken, pattern="order_chicken"))
dispatcher.add_handler(CallbackQueryHandler(order_chicks, pattern="order_chicks"))
dispatcher.add_handler(CallbackQueryHandler(chicks_plus, pattern="chicks_plus"))
dispatcher.add_handler(CallbackQueryHandler(chicks_minus, pattern="chicks_minus"))
dispatcher.add_handler(CallbackQueryHandler(order_breasts, pattern="order_breasts"))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), selector))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
