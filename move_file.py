import os
import shutil
from string import punctuation


current_dir = os.getcwd()

DOWNLOAD_FOLDER = "Downloads"


def create_dir(dir_path):
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)


def get_filtered_title(title):
    title_list = title.split(" ")

    filtered_title = []

    for word in title_list:
        if word.isalnum():
            filtered_title.append(word)
        else:
            clean_word = ""

            for letter in list(word):
                if letter not in punctuation:
                    clean_word += letter

            filtered_title.append(clean_word)

    filtered_title_str = " ".join(filtered_title)

    return filtered_title_str


def move_files(manga_title, chapter_name, file_name):

    manga_title_str = get_filtered_title(manga_title)
    # chapter_name_str = get_filtered_title(chapter_name)

    # manga_title_dir = f"{current_dir}\\{DOWNLOAD_FOLDER}\\{manga_title}"
    # manga_chapter_dir = f"{current_dir}\\{DOWNLOAD_FOLDER}\\{manga_title}\\{chapter_name}"

    manga_title_dir = f"{current_dir}\\{DOWNLOAD_FOLDER}\\{manga_title_str}"
    manga_chapter_dir = f"{current_dir}\\{DOWNLOAD_FOLDER}\\{manga_title_str}\\{chapter_name}"

    create_dir(DOWNLOAD_FOLDER)
    create_dir(manga_title_dir)
    create_dir(manga_chapter_dir)

    if os.path.isfile(f"{current_dir}\\{file_name}") and not os.path.isfile(f"{manga_chapter_dir}\\{file_name}"):
        source = f"{current_dir}\\{file_name}"
        destination = manga_chapter_dir

        shutil.move(source, destination)
