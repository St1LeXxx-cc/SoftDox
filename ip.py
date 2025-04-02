import os
import platform
import requests
from colorama import init, Fore

# Инициализация colorama (для Windows это обязательно)
init(autoreset=True)

HISTORY_FILE = "history.txt"  # Файл для сохранения истории

def clear_console():
    """Очищает консоль в зависимости от операционной системы"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def show_banner():
    """Отображает баннер 'COMETE'"""
    clear_console()
    print("=" * 54)
    print(" ██████╗ ██████╗ ███╗   ███╗███████╗████████╗███████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝")
    print("██║     ██║   ██║██╔████╔██║█████╗     ██║   █████╗")
    print("██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ███████╗")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝")
    print("=" * 54)

def save_to_history(ip, data):
    """Сохраняет IP-адрес и данные в файл истории"""
    with open(HISTORY_FILE, mode="a", encoding="utf-8") as file:
        file.write(f"IP: {ip}\n")
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        file.write("=" * 40 + "\n")

def search_by_ip(ip):
    """Получает информацию о местоположении по IP с использованием API"""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "success":
            print(f"\nИнформация о IP: {ip}")
            print(f"{Fore.GREEN}Страна: {data['country']}")
            print(f"{Fore.GREEN}Регион: {data['regionName']}")
            print(f"{Fore.GREEN}Город: {data['city']}")
            print(f"{Fore.GREEN}Провайдер: {data['isp']}")
            print(f"{Fore.GREEN}Широта: {data['lat']}")
            print(f"{Fore.GREEN}Долгота: {data['lon']}")
            save_to_history(ip, data)  # Сохраняем данные в историю
        else:
            print(Fore.RED + "\nIP-адрес не найден или неверный. Попробуйте снова.")
    except Exception as e:
        print(Fore.RED + f"\nПроизошла ошибка: {e}")

def display_menu():
    """Выводит меню программы"""
    print(Fore.CYAN + "\nМеню:")
    print("[1] Найти по IP")
    print("[0] Выход")

def main():
    """Основная логика программы"""
    while True:
        show_banner()
        display_menu()
        choice = input(Fore.YELLOW + "\nВыберите опцию: ")

        if choice == "1":
            ip = input(Fore.YELLOW + "\nВведите IP-адрес: ").strip()
            search_by_ip(ip)
            input(Fore.CYAN + "\nНажмите Enter, чтобы вернуться в меню...")
        elif choice == "0":
            print(Fore.GREEN + "\nВыход из программы. До свидания!")
            break
        else:
            print(Fore.RED + "\nНекорректный выбор. Попробуйте снова.")
            input(Fore.CYAN + "\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()