import sys
from pathlib import Path

# константи
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
TXT_DOCUMENTS = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'ZIP': ARCHIVES,
    'TXT': TXT_DOCUMENTS,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper() # Перетворення розширення файлу на назву папки

def scan(folder: Path) -> None: #ітеруємся по папці
    for item in folder.iterdir():
        if item.is_dir(): # якщо це папка, добавляємо її до списка і переходимо до наступного елементу + перевірка на дубляж
            if item.name not in ('archives','video','audio','documents','images','MY_OTHER'):
                FOLDERS.append(item)
                # скануэмо вкладену папку
                scan(item) # рекурсія
            continue 
        # робота з файлом
        ext = get_extension(item.name) # беремо розширення файлу
        fullname = folder / item.name # беремо шлях до фалу
        if not ext: # якщо файл нема розширення, додаємо до невідомих
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                # якщо не зареэстрували розширення у регістр додаємо до невідомих
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)

if __name__ == '__main__':
    folder_to_scan = sys.argv[1]
    scan(Path(folder_to_scan))