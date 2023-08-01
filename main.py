from scrape import *
from move_file import *
from download_manga import *
from argparse import ArgumentParser


def run_download_manga(manga_url, min_chapter, max_chapter, page):
    manga_title, manga_chapter_list = scrape_website(
        manga_url, min_chapter, max_chapter, page)

    download_manga(manga_title=manga_title,
                   manga_chapter_list=manga_chapter_list)


parser = ArgumentParser()

parser.usage = "Berikut adalah perintah yang dapat digunakan:"

parser.add_argument(
    "-l", "--link", help="URL dari manga yang akan diunduh", type=str, required=True)

parser.add_argument(
    "-p", "--page", help="Pilihan unduh manga", type=str, required=True, choices=["all", "custom"])

parser.add_argument(
    "--min", help="Chapter pertama manga yang akan diunduh", type=int)

parser.add_argument(
    "--max", help="Chapter terakhir manga yang akan diunduh", type=int)

args = parser.parse_args()

if args.page == "all":
    run_download_manga(args.link, args.min, args.max, args.page)
elif args.page == "custom":
    if args.min == None or args.max == None:
        print("[!] Input salah! Program selesai!")
        print("[!] Tambahkan min dan max chapter!")
        exit()

    run_download_manga(args.link, args.min, args.max, args.page)
else:
    print("[!] Input salah! Program selesai!")
    exit()
