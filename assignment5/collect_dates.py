# UiO: IN4110 - H20
# Assignment 5.3
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no

import re
import requests as req


def find_dates(html, output=None):
    """
    :param html: str: String with the HTML from a given website.
    :param output: str: Name of the output file to be saved.

    :return: list: A list of all dates found in the html in the
                   following format (year/month/day).
    """
    # scrapping url
    request = req.get(html)
    assert request.status_code == 200

    # defining patterns
    ISO = r'((?:1\d{3}|2\d{3})\-(?:0[1-9]|1[0-2])' \
          r'\-(?:0[1-9]|1[0-9]|2[0-9]|3[0-1]))'

    DMY_MDY_MY = r'((?:0[1-9]|1[0-9]|2[0-9]|3[0-1])?\s?(?:January|Jan' \
                 r'|February|Feb|March|Mar|April|Apr|May|June|Jun|July' \
                 r'|Jul|August|Aug|September|Sept|Sep|October|Oct|' \
                 r'November|Nov|December|Dec)\s?(?:0?[1-9]|1[0-9]|2[0-9]' \
                 r'|3[0-1])?\,?\s(?:1\d{3}|2\d{3}))'

    YMD_YM = r'((?:1\d{3}|2\d{3})\s(?:January|Jan|February|Feb|March|Mar' \
             r'|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept' \
             r'|Sep|October|Oct|November|Nov|December|Dec)' \
             r'\s(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])?)'

    regexes = [ISO, DMY_MDY_MY, YMD_YM]

    # getting all dates
    found_dates = []
    for regex in regexes:
        found_dates += re.findall(pattern=regex, string=request.text)

    # fixing wrong ',', '-' and spaces
    regex_in = [r'\,', r'^\s', r'\s$', r'\-']
    regex_out = [r'', r'', r'', r'/']
    for in_, out_ in zip(regex_in, regex_out):
        for idx, str_ in enumerate(found_dates):
            found_dates[idx] = re.sub(pattern=in_, repl=out_, string=str_)

    # defining patterns
    DMY = r'(0?[1-9]|1[0-9]|2[0-9]|3[0-1])\s(January|Jan|February|Feb' \
          r'|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|' \
          r'September|Sept|Sep|October|Oct|November|Nov|December|Dec)' \
          r'\s(1\d{3}|2\d{3})'

    MDY = r'(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun' \
          r'|July|Jul|August|Aug|September|Sept|Sep|October|Oct|November' \
          r'|Nov|December|Dec)' \
          r'\s(0?[1-9]|1[0-9]|2[0-9]|3[0-1])' \
          r'\s(1\d{3}|2\d{3})'

    MY = r'(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun' \
         r'|July|Jul|August|Aug|September|Sept|Sep|October|Oct|November' \
         r'|Nov|December|Dec)' \
         r'\s(1\d{3}|2\d{3})'

    YM = r'(1\d{3}|2\d{3})' \
         r'\s(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun' \
         r'|July|Jul|August|Aug|September|Sept|Sep|October|Oct|November' \
         r'|Nov|December|Dec)'

    YMD = r'(1\d{3}|2\d{3})' \
          r'\s(January|Jan|February|Feb|March|Mar|April|Apr|May|June|Jun' \
          r'|July|Jul|August|Aug|September|Sept|Sep|October|Oct|November' \
          r'|Nov|December|Dec)' \
          r'\s(0?[1-9]|1[0-9]|2[0-9]|3[0-1])'

    regex_in = [DMY, MDY, MY, YM, YMD]
    regex_out = [r'\3/\2/\1', r'\3/\1/\2', r'\2/\1', r'\1/\2', r'\1/\2/\3']

    # replacing elements to the format YYYY/MM/DD
    for in_, out_ in zip(regex_in, regex_out):
        for idx, str_ in enumerate(found_dates):
            found_dates[idx] = re.sub(pattern=in_, repl=out_, string=str_)

    # defining patterns
    regex_in = [r'(January|Jan)', r'(February|Feb)', r'(March|Mar)',
                r'(April|Apr)', r'(May)', r'(June|Jun)',
                r'(July|Jul)', r'(August|Aug)', r'(September|Sept|Sep)',
                r'(October|Oct)', r'(November|Nov)', r'(December|Dec)']

    regex_out = [r'01', r'02', r'03', r'04', r'05', r'06', r'07', r'08',
                 r'09', r'10', r'11', r'12']

    # replacing months to digits
    for in_, out_ in zip(regex_in, regex_out):
        for idx, str_ in enumerate(found_dates):
            found_dates[idx] = re.sub(pattern=in_, repl=out_, string=str_)

    # writing the output file
    if output is not None:
        with open(file=f'filter_dates_regex/{output}.txt',
                  mode='a+', encoding='utf-8') as file:
            for line in found_dates:
                file.write(line + '\n')

    return found_dates


if __name__ == "__main__":
    urls = ["https://en.wikipedia.org/wiki/Linus_Pauling",
            "https://en.wikipedia.org/wiki/Rafael_Nadal",
            "https://en.wikipedia.org/wiki/J._K._Rowling",
            "https://en.wikipedia.org/wiki/Richard_Feynman",
            "https://en.wikipedia.org/wiki/Hans_Rosling"]

    name = ['Linus_Pauling', 'Rafael_Nadal', 'Rowling',
            'Richard_Feynman', 'Hans_Rosling']

    for url, name in zip(urls, name):
        find_dates(url, output=name)
