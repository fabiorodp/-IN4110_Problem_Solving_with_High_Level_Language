# UiO: IN4110 - H20
# Assignment 5.2
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no

import re
from assignment5.requesting_urls import get_html


def find_urls(html, base_url='https://en.wikipedia.org'):
    """
    Simple function to get all urls from a HTML string.

    :param html: str: The HTML code of a given website.
    :param base_url: str: Base website to complete relative's urls.

    :return: list: List containing all urls that was found.
    """
    if isinstance(html, str) is not True:
        raise ValueError("Error: html must be string type.")

    resp = re.findall(
        pattern=r"\<a\s[^\>]*href=[\"https?](?:(?!\#))([^\"]*)",
        string=html)

    for idx, i in enumerate(resp):
        if (i[0] == '/') and (i[1] == '/'):
            resp[idx] = base_url + resp[idx][1:]
        elif (i[0] == '/') and (i[1] != '/'):
            resp[idx] = base_url + resp[idx]

    return resp


def find_articles(html, base_url='https://en.wikipedia.org'):
    """
    Simple function to get all articles from a given wikipedia
    website.

    :param html: str: The HTML code of a given website.
    :param base_url: str: Base website to complete relative's urls.

    :return: list: List containing all articles that was found.
    """
    found_urls = find_urls(html=html, base_url=base_url)
    lst_articles = []
    for url in found_urls:
        resp = re.findall(
            pattern=r"(?:^\w.*\/wiki\/(?!File:|Help:|Template:|Special:"
                    r"|Wikipedia:|Category:|Portal:|Talk:|\%|"
                    r"Cookie_statement|Privacy_policy|Main_Page"
                    r"|Case_sensitivity|Terms_of_Use)\w.*)",
            string=url)

        if resp:
            lst_articles.append(resp[0])

    return lst_articles


if __name__ == "__main__":
    base = 'https://en.wikipedia.org'

    urls = [r'https://en.wikipedia.org/wiki/Nobel_Prize',
            r'https://en.wikipedia.org/wiki/Bundesliga',
            r'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski']

    names = ['Nobel_Prize', 'Bundesliga', 'Alpine_Ski']

    for url, name in zip(urls, names):
        html = get_html(url, params=None, output=None)

        # saving urls
        found_articles = find_articles(html.text, base_url=base)
        with open(file='filter_urls/articles_{}.txt'.format(name),
                  mode='a+', encoding='utf-8') as file:
            for i in found_articles:
                file.write(i + '\n')
