import time
import mimetypes
from yaspin import yaspin
from requests_html import HTMLSession

from scrape import *
from move_file import *

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

DELAY_TIME = 60

session = HTMLSession()

def download_manga(manga_title, manga_chapter_list):
    print(f"\n🚀 {manga_title} 🚀\n")

    for chapter_name, chapter_url in manga_chapter_list.items():
        print(f"[INFO]: ✨ Mengunduh {chapter_name} ✨\n")

        r = session.get(chapter_url, timeout=360)

        r.html.render(timeout=360)

        chapters = r.html.find(".ts-main-image")

        for index, chapter in enumerate(chapters):

            manga_panel_url = chapter.attrs["src"]

            manga_request = requests.get(
                manga_panel_url, stream=True, timeout=360, allow_redirects=True, headers=headers)

            content_type = manga_request.headers.get("content-type")

            extension = mimetypes.guess_extension(content_type)

            if "html" in content_type.lower() or "text" in content_type.lower():
                pass
            else:
                file_name = f"{index}{extension}"

                with yaspin(text="Loading ...", color="green") as sp:
                    with open(f"{file_name}", "wb") as manga_file:
                        for ch in manga_request.iter_content(chunk_size=1024):
                            if ch:
                                manga_file.write(ch)
                                manga_file.flush()

                    sp.write(f"[INFO]: ✅ {file_name} [SELESAI]")

                # Move downloaded files ...

                move_files(manga_title=manga_title,
                        chapter_name=chapter_name, file_name=file_name)

        print(f"\n[INFO]: 🔥 {chapter_name} [SELESAI]\n")

        if not list(manga_chapter_list.keys())[-1] == chapter_name:
            with yaspin(text=f"Delay {DELAY_TIME} detik ...", color="yellow") as sp:
                time.sleep(DELAY_TIME)
                sp.write("[INFO]: ⏰ delay [SELESAI]\n")

    print(f"[INFO]: 🤩 {manga_title} [SELESAI] 🎉\n")

