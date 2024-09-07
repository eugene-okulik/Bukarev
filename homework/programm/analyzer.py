import os
import argparse


def find_text_in_line(line, search_text):
    words = line.split()
    if search_text in words:
        index = words.index(search_text)
        start = max(0, index - 5)
        end = min(len(words), index + 6)
        context = ' '.join(words[start:end])
        return context
    return None


def search_in_file(file_path, search_text, find_first):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line_number, line in enumerate(lines, start=1):
            found_text = find_text_in_line(line, search_text)
            if found_text:
                print(f"Файл: {file_path}, строка: {line_number}")
                print(f"Контекст: {found_text}\n")
                if find_first:
                    break


def search_in_logs_directory(logs_directory, search_text, find_first):
    if os.path.isdir(logs_directory):
        files_in_directory = os.listdir(logs_directory)
        if files_in_directory:
            for filename in files_in_directory:
                file_path = os.path.join(logs_directory, filename)
                if os.path.isfile(file_path):
                    search_in_file(file_path, search_text, find_first)
                else:
                    print(f"{file_path} не является файлом.")
        else:
            print("Папка пуста.")
    else:
        print(f"Директория {logs_directory} не найдена или не является папкой.")


def main():
    parser = argparse.ArgumentParser(description="Программа для поиска текста в лог-файлах из указанной папки.")
    parser.add_argument("log_directory", type=str, help="Полный путь к папке с файлами логов")
    parser.add_argument("--text", type=str, required=True, help="Текст, который нужно найти в файлах")
    parser.add_argument("--first", action="store_true", help="Найти только первое совпадение")
    args = parser.parse_args()
    search_in_logs_directory(args.log_directory, args.text, args.first)


if __name__ == "__main__":
    main()
