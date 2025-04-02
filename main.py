import os
import subprocess
import sys  # Необходимо для установки модулей через subprocess

def install_modules():
    # Добавьте необходимые модули в этот список
    required_modules = ["termcolor", "faker", "requests", "pandas"]
    for module in required_modules:
        try:
            __import__(module)  # Проверка: установлен ли модуль
        except ImportError:
            print(f"\nМодуль '{module}' не установлен. Устанавливаю...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"Модуль '{module}' успешно установлен!")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    clear_screen()
    print("=" * 54)
    print(" ██████╗ ██████╗ ███╗   ███╗███████╗████████╗███████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝")
    print("██║     ██║   ██║██╔████╔██║█████╗     ██║   █████╗")
    print("██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ███████╗")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝")
    print("=" * 54)
    print(" [1] Создать бота         [2] Информация о номере")
    print(" [3] Мануалы              [4] Фэйк инфо  ")
    print(" [5] Поиск по ФИО         [6] Поиск по IP  ")
    print("=" * 54)
    print("                   [99] Об программе")
    print("                   [100] Антивирус")
    print("                   [0] Выход")
    print("=" * 54)

def about_program():
    clear_screen()
    print("=" * 54)
    print("                 Об программе")
    print("=" * 54)
    print("            Автор: Orionchik")
    print("            Канал: WsOrion")
    print("            Гит хаб: Скоро")
    print("            Версия: платная(средняя)")
    print("=" * 54)
    input("\nНажмите Enter, чтобы вернуться в меню...")

def main():
    install_modules()  # Устанавливаем модули перед запуском меню
    while True:
        show_menu()
        choice = input("\n Выберите опцию: ")
        if choice == "1":
            try:
                subprocess.run(['python', 'tgbot.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "2":
            try:
                subprocess.run(['python', 'number.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "3":
            try:
                subprocess.run(['python', 'manual.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "4":
            try:
                subprocess.run(['python', 'fake.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "5":
            try:
                subprocess.run(['python', 'fio.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "6":
            try:
                subprocess.run(['python', 'ip.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "100":
            try:
                subprocess.run(['python', 'bez.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Произошла ошибка при запуске второго файла: {e}")
                input("\nНажмите Enter, чтобы вернуться...")
        elif choice == "99":
            about_program()
        elif choice == "0":
            print("\nВыход...")
            break
        else:
            print("\nНеверная опция. Попробуйте снова.")
            input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()
