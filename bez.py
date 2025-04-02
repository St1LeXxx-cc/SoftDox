import os


def clear_console():
    """Очищает консоль в зависимости от операционной системы"""
    if os.name == "nt":  # Для Windows
        os.system("cls")
    else:  # Для Linux и MacOS
        os.system("clear")

def show_banner():
    """Отображает баннер COMETA"""
    print("=" * 54)
    print(" ██████╗ ██████╗ ███╗   ███╗███████╗████████╗███████╗")
    print("██╔════╝██╔═══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝")
    print("██║     ██║   ██║██╔████╔██║█████╗     ██║   █████╗")
    print("██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║   ██╔══╝")
    print("╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║   ███████╗")
    print(" ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝")
    print("                     COMETA                   ")
    print("=" * 54)

def play_melody():
    """Воспроизводит мелодию при запуске программы"""
    try:
        pygame.mixer.init()  # Инициализация аудиосистемы
        pygame.mixer.music.load("melody.mp3")  # Указываем путь к вашему файлу
        pygame.mixer.music.play()
        print("[INFO] Воспроизведение мелодии...")
        while pygame.mixer.music.get_busy():  # Ожидание завершения воспроизведения
            pass
    except Exception as e:
        print(f"[Ошибка] Не удалось воспроизвести звук: {e}")

def scan_files(suspicious_keywords):
    """Сканирует все файлы на устройстве на наличие подозрительных строк"""
    print("Начало сканирования всех файлов на устройстве...")
    root_directory = "/" if os.name != "nt" else "C:\\"  # Стартовая директория для сканирования
    suspicious_files = []

    # Проход по всем файлам в файловой системе
    for root, _, files in os.walk(root_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, mode="r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    for keyword in suspicious_keywords:
                        if keyword.lower() in content.lower():
                            suspicious_files.append(file_path)
                            print(f"[УГРОЗА] Найдено в файле: {file_path}")
                            break
            except PermissionError:
                print(f"[ОШИБКА ДОСТУПА] Нет доступа к файлу: {file_path}")
            except Exception as e:
                print(f"[ОШИБКА] Не удалось обработать файл {file_path}: {e}")

    if suspicious_files:
        print("\nСканирование завершено. Найдены подозрительные файлы:")
        for suspicious_file in suspicious_files:
            print(suspicious_file)
    else:
        print("\nСканирование завершено. Угроз не обнаружено.")

def main():
    """Основная логика программы"""
    clear_console()
    play_melody()  # Воспроизводим мелодию перед запуском
    while True:
        show_banner()
        print("\nМеню:")
        print("[1] Сканировать все файлы на устройстве")
        print("[0] Выход")
        choice = input("\nВыберите опцию: ")

        if choice == "1":
            suspicious_keywords = ["malware", "virus", "trojan", "attack", "hacked"]  # Ключевые слова для поиска
            scan_files(suspicious_keywords)
            input("\nНажмите Enter, чтобы вернуться в меню...")
        elif choice == "0":
            print("\nВыход из программы. До свидания!")
            break
        else:
            print("\nНекорректный выбор. Попробуйте снова.")
            input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()