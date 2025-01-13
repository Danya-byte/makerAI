import os

# Папки, которые нужно игнорировать
IGNORE_DIRS = [
    'node_modules',  # Папка с зависимостями Node.js
    'venv',  # Виртуальное окружение Python
    '.git',  # Папка Git
    '__pycache__',  # Кэш Python
    '.vscode',  # Папка настроек VS Code
    '.idea',  # Папка настроек PyCharm/IntelliJ
    'dist',  # Папка сборки (если используется)
    'build',  # Папка сборки (если используется)
]


def print_project_structure(start_path, ignore_dirs, prefix=""):
    """Рекурсивно выводит структуру проекта."""
    if not os.path.isdir(start_path):
        print(f"{prefix}📄 {os.path.basename(start_path)}")
        return

    print(f"{prefix}📁 {os.path.basename(start_path)}")
    prefix += "    "

    for item in sorted(os.listdir(start_path)):
        item_path = os.path.join(start_path, item)
        if os.path.isdir(item_path) and item in ignore_dirs:
            continue  # Пропускаем игнорируемые папки
        print_project_structure(item_path, ignore_dirs, prefix)


if __name__ == "__main__":
    project_path = os.getcwd()  # Текущая директория (можно заменить на путь к проекту)
    print(f"Структура проекта: {project_path}")
    print_project_structure(project_path, IGNORE_DIRS)
