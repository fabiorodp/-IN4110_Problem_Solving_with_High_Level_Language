# UiO: IN4110 - H20
# Assignment 5.4
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no

from bs4 import BeautifulSoup
import requests as req
import re
import dateutil


def extract_events(url, file_path_name=None):
    """
    Function to extract date, venue, discipline of an url.

    :param url: str: URL of the website to be scraped.
    :param file_path_name: dict: Path and name of the file to be saved.

    :return data: dict: Containing the date, venue, discipline and empty tip.
    """
    # checking if the request returned positive
    request = req.get(url)
    assert request.status_code == 200

    # parsing html to bs4
    website = BeautifulSoup(request.content, 'lxml')

    # getting the targeted tables for men, ladies and team calendars
    tables = website.find_all(
        name='table',  # tag
        attrs={'class': 'plainrowheaders'})

    # getting the header of the table:
    headers, columns = ['Date', 'Venue', 'Type'], [2, 3, 4]
    data = {'Date': [], 'Venue': [], 'Discipline': [], 'Tip': []}

    for table in tables:
        # checking if bs4 got the correct table
        header = table.find_all(name='th')
        for h, c in zip(headers, columns):
            assert re.search(
                pattern=h, string=header[c].get_text()) is not None

        # getting rows' contents
        rows = table.find_all(name='tr')
        for r in rows[1:]:
            # getting data from a row
            cells = r.find_all(name='td')

            for cell in cells:
                if cell.find('span') is not None:
                    venue_txt = cell.get_text(strip=True)
                    data['Venue'].append(venue_txt)

                elif cell.has_attr('align'):
                    if cell.attrs['align'] == 'right':
                        txt = cell.get_text(strip=True)

                        if len(txt) > 10:
                            date_txt = re.findall(pattern=r'[\w\s]+',
                                                  string=txt)
                            if len(date_txt) > 1:
                                date_txt = dateutil.parser.parse(date_txt[1])
                                data['Date'].append(date_txt)

                            else:
                                date_txt = dateutil.parser.parse(date_txt[0])
                                data['Date'].append(date_txt)

                        else:
                            discipline_txt = re.findall(pattern=r'[A-Z]+',
                                                        string=txt)
                            data['Discipline'].append(discipline_txt[0])

                            if len(data['Discipline']) != len(data['Venue']):
                                venue_txt = data['Venue'][-1]
                                data['Venue'].append(venue_txt)

                            data['Tip'].append('          ')

                            break

    if file_path_name is not None:
        save_table(file_path_name=file_path_name, data=data)

    return data


def save_table(file_path_name, data):
    """
    Function to generate an empty betting split.

    :param file_path_name: str: Path and name of the file to be saved.
    :param data: dict: Containing the date, venue, discipline and empty tip.
    """
    with open(file=f'{file_path_name}', mode='a+', encoding='utf-8') as file:
        file.write('Betting slip\n')
        file.write('\nName:\n\n')

        hds = ['Dates:                   ', 'Venues:                  ',
               'Disciplines:             ', 'Who wins?                ']

        for idx, h in enumerate(hds):
            if idx == 0:
                file.write(f'|{h}|')
            else:
                file.write(f'{h}|')

        file.write('\n')

        for idx, h in enumerate(hds):
            dashes = ''

            for _ in range(len(h)):
                dashes += '-'

            if idx == 0:
                file.write(f'|{dashes}|')
            else:
                file.write(f'{dashes}|')

        file.write('\n')

        for d, v, dc, t in zip(data['Date'], data['Venue'],
                               data['Discipline'], data['Tip']):

            len_v = len(v)
            for _ in range(25-len_v):
                v += ' '

            len_dc = len(dc)
            for _ in range(25 - len_dc):
                dc += ' '

            len_t = len(t)
            for _ in range(25 - len_t):
                t += ' '

            file.write(f'|{d}      |{v}|{dc}|{t}|\n')


if __name__ == '__main__':
    urls = ['https://en.wikipedia.org/wiki/2019%E2%80%9320'
            '_FIS_Alpine_Ski_World_Cup',
            'https://en.m.wikipedia.org/wiki/2020%E2%80%9321'
            '_FIS_Alpine_Ski_World_Cup']

    file_names = ['datetime_filter/betting_slip_empty1.md',
                  'datetime_filter/betting_slip_empty2.md']

    for url, file_name in zip(urls, file_names):
        extract_events(url=url, file_path_name=file_name)
