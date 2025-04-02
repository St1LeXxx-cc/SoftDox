import csv
import os
import platform
import time
import threading
from colorama import init, Fore, Style

# Инициализация colorama (для работы цвета текста)
init(autoreset=True)

def clear_console():
    """Очищает консоль в зависимости от операционной системы"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def show_banner():
    """Отображает баннер программы"""
    clear_console()
    print("=" * 54)
    print(" ██████╗ ██████╗ ███╗   ███╗███████╗████████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝")
    print("██║     ██║   ██║██╔████╔██║█████╗     ██║   ")
    print("██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ")
    print("     ПОИСК ФИО В УКАЗАННЫХ CSV ФАЙЛАХ         ")
    print("=" * 54)

def read_csv_files(search_value, stop_event):
    """Считывает фиксированный список CSV-файлов и ищет совпадения по ФИО"""
    results = []
    csv_files = ["data.csv", "one.csv"]  # Укажите свои файлы

    for file_path in csv_files:
        try:
            with open(file_path.strip(), mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    full_name = " ".join([row.get("Имя", ""), row.get("Фамилия", ""), row.get("Отчество", "")]).strip()
                    if full_name.lower() == search_value.lower():
                        results.append({"file": file_path, "data": row})
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден. Проверьте правильность пути.")
        except Exception as e:
            print(f"Ошибка при чтении файла '{file_path}': {e}")
    stop_event.set()
    return results

def spinner(stop_event):
    """Анимация индикатора ожидания"""
    symbols = ['|', '/', '-', '\\']
    while not stop_event.is_set():
        for symbol in symbols:
            print(f"\r{Fore.YELLOW}Поиск {symbol}", end="")
            time.sleep(0.2)

def main():
    while True:
        show_banner()
        print("\nМеню:")
        print("[1] Искать ФИО")
        print("[0] Выход")
        
        choice = input("\nВыберите опцию: ")
        if choice == "1":
            search_value = input("\nВведите ФИО для поиска (например, Иван Иванов Иванович): ").strip()
            print(f"\nФИО: {search_value}\n")  # Пропуск одной строки

            if not search_value:
                print("Вы не ввели ФИО. Попробуйте снова.")
                input("\nНажмите Enter, чтобы продолжить...")
                continue

            # Создаём событие для остановки индикатора ожидания
            stop_event = threading.Event()
            spinner_thread = threading.Thread(target=spinner, args=(stop_event,))
            spinner_thread.start()

            # Выполняем поиск
            results = read_csv_files(search_value, stop_event)

            # Ждём завершения индикатора
            spinner_thread.join()
            clear_console()

            if results:
                print("\nНайденные результаты:")
                for result in results:
                    print(f"Файл: {result['file']}, Данные: {result['data']}")
            else:
                print("\nСовпадений не найдено.")
            input("\nНажмите Enter, чтобы вернуться в меню...")
        elif choice == "0":
            print("\nВыход из программы. До свидания!")
            break
        else:
            print("\nНекорректный выбор. Попробуйте снова.")
            input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()