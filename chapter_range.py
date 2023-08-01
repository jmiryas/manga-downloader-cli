# Mengecek apakah string merupakan angka atau bukan

def is_number(chapter_number):
    if isinstance(chapter_number, int):
        return True

    if isinstance(chapter_number, float):
        return True

    if chapter_number.isdigit():
        return True
    else:
        try:
            float(chapter_number)
            return True
        except ValueError:
            return False


# Mendapatkan chapter number dalam bentuk string

def get_chapter_number(chapter_name):
    chapter_number = chapter_name.split(" ").pop()

    return chapter_number


# Mengubah chapter number dalam bentuk string menjadi number int atau float

def get_chapter_number_converted(chapter_number_str):
    if chapter_number_str.isdigit():
        int_number = int(chapter_number_str)
        return int_number
    else:
        try:
            float_number = float(chapter_number_str)
            return float_number
        except ValueError:
            pass


# Mendapatkan min dan max chapter number dari hasil scraping

def get_min_max_chapter_number(chapter_list):
    chapter_number_list = list(chapter_list.keys())

    chapter_number_converted_list = []

    for number in chapter_number_list:
        chapter_number_str = get_chapter_number(number)

        if is_number(chapter_number_str):
            chapter_number_converted = get_chapter_number_converted(
                chapter_number_str)

            chapter_number_converted_list.append(chapter_number_converted)

    min_chapter = min(chapter_number_converted_list)
    max_chapter = max(chapter_number_converted_list)

    return min_chapter, max_chapter


# Mendapatkan chapter manga dalam bentuk range
# Contoh: Chapter 5 - 10

def get_chapter_range(first_chapter, last_chapter, min_chapter, max_chapter, chapter_list):
    if not is_number(min_chapter) or not is_number(max_chapter):
        print("[INFO]: Input salah! Program berhenti!")
        exit()

    if min_chapter < first_chapter or min_chapter > last_chapter or max_chapter < first_chapter or max_chapter > last_chapter or min_chapter > max_chapter or max_chapter < min_chapter:
        print("[INFO]: Input salah! Program berhenti!")
        exit()

    chapter_manga_range = {}

    for index, value in chapter_list.items():
        chapter_number = get_chapter_number(index)

        if is_number(chapter_number):
            chapter_number_converted = get_chapter_number_converted(
                chapter_number)

            if chapter_number_converted >= min_chapter and chapter_number_converted <= max_chapter:
                chapter_manga_range[index] = value

    sorted_manga_range = dict(sorted(chapter_manga_range.items()))

    return sorted_manga_range
