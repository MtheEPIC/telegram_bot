from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import logging

from funcs import start, help, add_group, unknown, stop
from order import order, order_beef, order_chicken, order_chicks, order_breasts, \
    order_product, order_entrecote, order_butcher_cut
from gallery import gallery, gallery_all, gallery_beef, gallery_chicken
from utiles import get_key, put

previous = None
product = None


def selector(update: Update, context: CallbackContext):
    global previous, product

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
    elif update.message.text == 'chicken':
        if previous == 'gallery':
            gallery_chicken(update, context)
        elif previous == 'order':
            order_chicken(update, context)

    elif update.message.text == 'entrecote':
        product = 'entrecote'
        order_entrecote(update, context)
    elif update.message.text == 'butcher cut':
        product = 'butcher cut'
        order_butcher_cut(update, context)
    elif update.message.text == 'chicks':
        product = 'chicks'
        order_chicks(update, context)
    elif update.message.text == 'breasts':
        product = 'breasts'
        order_breasts(update, context)

    elif update.message.text == '+':
        put(update, context, product, +1)
        order_product(update, context, product)
    elif update.message.text == '-':
        put(update, context, product, -1)
        order_product(update, context, product)

    previous = update.message.text


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(get_key(), use_context=True)
    dispatcher = updater.dispatcher

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
    # dispatcher.add_handler(CallbackQueryHandler(chicks_plus, pattern="chicks_plus"))
    # dispatcher.add_handler(CallbackQueryHandler(chicks_minus, pattern="chicks_minus"))
    dispatcher.add_handler(CallbackQueryHandler(order_breasts, pattern="order_breasts"))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), selector))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()
