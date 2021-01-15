# UiO: IN4110 - H20
# Assignment 5.1
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no

import requests as req
import threading


def get_html(url, params=None, output=None):
    """
    Simple scrapping function for websites.

    :param url: str: The url of the website.
    :param params: dict: Key/value of the url's parameters.
    :param output: str: The name of the txt output file where
                        the html code will be saved.

    :return: class object: The response of the requested url.
    """
    if params is not None:
        if isinstance(params, dict) is not True:
            raise ValueError('Error: Argument params '
                             'must be dictionary with '
                             'key/values.')

    if output is not None:
        with open(file='requesting_urls/{}.txt'.format(output),
                  mode='a+', encoding='utf-8') as file:
            response = req.get(url, params=params)
            file.write(response.url+'\n')
            file.write(response.text+'\n')
        return response

    else:
        return req.get(url, params=params)


if __name__ == "__main__":
    urls = [r'https://en.wikipedia.org/wiki/Studio_Ghibli',
            r'https://en.wikipedia.org/wiki/Star_Wars',
            r'https://en.wikipedia.org/wiki/Dungeons_%26_Dragons',
            r'https://en.wikipedia.org/wiki/Main_Page',
            r'https://en.wikipedia.org/wiki/Main_Page']

    params = [None, None, None, {'title': 'Main Page', 'action': 'info'},
              {'title': 'Hurricane_Gonzalo', 'oldid': '983056166'}]

    outputs = ['output_Studio_Ghibli', 'output_Star_Wars',
               'output_Dungeons_%26_Dragons', 'output_Main_Page_info',
               'output_Main_Page_Gonzalo']

    for u, p, o in zip(urls, params, outputs):
        t = threading.Thread(target=get_html, args=(u, p, o,))
        t.start()
        t.join()
