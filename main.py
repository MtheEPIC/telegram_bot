from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging

from funcs import start, help, gallery, add_group, bt_help, unknown, bt_start, bt_gallery, bt_gallery_all, \
    bt_gallery_chicken, bt_gallery_beef, bt_stop
from order import bt_order, bt_order_chicken, bt_order_beef, order, bt_order_chicks, bt_order_breasts, chicks_plus, \
    chicks_minus
from utiles import get_key


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(get_key())
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('gallery', gallery))
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, add_group))
dispatcher.add_handler(CallbackQueryHandler(bt_start, pattern="bt_start"))
dispatcher.add_handler(CallbackQueryHandler(bt_stop, pattern="bt_stop"))
dispatcher.add_handler(CallbackQueryHandler(bt_help, pattern="bt_help"))
dispatcher.add_handler(CallbackQueryHandler(bt_gallery, pattern="bt_gallery"))
dispatcher.add_handler(CallbackQueryHandler(bt_gallery_chicken, pattern="gallery_chicken"))
dispatcher.add_handler(CallbackQueryHandler(bt_gallery_beef, pattern="gallery_beef"))
dispatcher.add_handler(CallbackQueryHandler(bt_gallery_all, pattern="gallery_all"))
dispatcher.add_handler(CommandHandler('order', order))
dispatcher.add_handler(CallbackQueryHandler(bt_order, pattern="bt_order"))
dispatcher.add_handler(CallbackQueryHandler(bt_order_beef, pattern="order_beef"))
dispatcher.add_handler(CallbackQueryHandler(bt_order_chicken, pattern="order_chicken"))
dispatcher.add_handler(CallbackQueryHandler(bt_order_chicks, pattern="order_chicks"))
dispatcher.add_handler(CallbackQueryHandler(chicks_plus, pattern="chicks_plus"))
dispatcher.add_handler(CallbackQueryHandler(chicks_minus, pattern="chicks_minus"))
dispatcher.add_handler(CallbackQueryHandler(bt_order_breasts, pattern="order_breasts"))

dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
