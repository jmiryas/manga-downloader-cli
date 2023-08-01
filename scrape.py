import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from chapter_range import *

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}


# Mendapatkan nama chapter dan melakukan konversi
# Contoh:
# Chapter 4 => Chapter 04
# chapter 5.5 => Chapter 05.5

def get_chapter_name(chapter_name):
    index_number = chapter_name.split(" ").pop()

    if index_number.isdigit():

        int_index = int(index_number)

        if int_index < 10:
            return f"Chapter 0{int_index}"
        else:
            return f"Chapter {int_index}"
    else:
        try:
            float_index = float(index_number)
            if float_index < 10:
                return f"Chapter: 0{float_index}"
            else:
                return f"Chapter: {float_index}"
        except ValueError:
            return chapter_name


def scrape_website(web_url, min_chapter, max_chapter, page="all"):
    manga_request = requests.get(web_url, headers=headers)

    soup = BeautifulSoup(manga_request.content, "html5lib")

    manga_title = soup.find("h1", attrs={"class": "entry-title"}).text

    episode_lister = soup.find("div", attrs={"class": "eplister"})

    episode_number_list = episode_lister.findAll(
        "div", attrs={"class": "eph-num"})

    manga_chapter_url = {}

    for episode in episode_number_list:
        chapter_name = get_chapter_name(episode.a.span.text)
        manga_chapter_url[chapter_name] = episode.a["href"]

    sorted_manga_chapter_url = dict(sorted(manga_chapter_url.items()))

    if page == "all":
        return manga_title, sorted_manga_chapter_url
    elif page == "custom":
        first_chapter, last_chapter = get_min_max_chapter_number(
            sorted_manga_chapter_url)

        manga_chapter_range = get_chapter_range(
            first_chapter, last_chapter, min_chapter, max_chapter, sorted_manga_chapter_url)

        return manga_title, manga_chapter_range

    else:
        print("[INFO]: Input salah! Program berhenti!")
        exit()
