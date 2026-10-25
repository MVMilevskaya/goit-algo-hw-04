import argparse
from pathlib import Path
import shutil
import sys

def parse_argv():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("-o", "--output", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def recursive_copy(source: Path, output: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy(el, output)
            elif el.is_file():
                extension = el.suffix[1:] if el.suffix else "no_extension"
                
                folder = output / extension
                folder.mkdir(exist_ok=True, parents=True)
                
                shutil.copy(el, folder)
                
    except Exception as e:
        print(f"Помилка при обробці папки {source}: {e}", file=sys.stderr)

def main():
    args = parse_argv()

    if not args.source.exists() or not args.source.is_dir():
        print(f"Помилка: Вихідна директорія '{args.source}' не існує або не є папкою.", file=sys.stderr)
        return

    print(f"Починаємо копіювання з '{args.source}' до '{args.output}'...")
    recursive_copy(args.source, args.output)
    print("Копіювання та сортування завершено успішно!")

if __name__ == "__main__":
    main()