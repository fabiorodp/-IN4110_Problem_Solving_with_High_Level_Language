# UiO: IN4110 - H20
# Assignment 5.5
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no

from bs4 import BeautifulSoup
import requests as req
import re
import dateutil
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def extract_url_teams(url):
    """
    Function to extract urls of the teams' which are in the semifinals.

    :param url: str: Website to be scrapped.

    :return teams_in_semifinals: list: Containing the teams in the
                                       semifinals.

    :return teams_url: list: Containing the teams' urls.
    """
    request = req.get(url)
    assert request.status_code == 200

    # parsing html to bs4
    website = BeautifulSoup(request.content, 'lxml')

    playoff_teams = ['Milwaukee', 'Orlando', 'Indiana', 'Miami', 'Boston',
                     'Philadelphia', 'Toronto', 'Brooklyn', 'LA Lakers',
                     'Portland', 'Houston', 'Oklahoma City', 'Denver', 'Utah',
                     'LA Clippers', 'Dallas']

    # getting the targeted tables for men, ladies and team calendars
    table = website.find(name='table',  # tag
                         attrs={'border': '0', 'cellpadding': '0'})

    # picking which team made it to the semi-finals:
    team_count = [table.text.count(team) for team in playoff_teams]
    teams_in_semifinals = [team for team, count in
                           zip(playoff_teams, team_count) if count >= 2]

    # picking the teams' url:
    teams_url = ['https://en.wikipedia.org' + table.find_all(
        name='a', text=team)[0]['href'] for team in teams_in_semifinals]

    return teams_in_semifinals, teams_url


def extract_url_players(team_url):
    """
    Function to extract urls of the players of a specific team.

    :param team_url: str: Website to be scrapped.

    :return players: list: Containing the players of the team.

    :return players_urls: list: Containing the players' urls.
    """
    request = req.get(team_url)
    assert request.status_code == 200

    # parsing html to bs4
    website = BeautifulSoup(request.content, 'lxml')

    table = website.find(name='table',
                         attrs={'class': 'toccolours'})

    cells = table.find_all(name='td', attrs={'style': 'text-align:left;'})
    players = [cell.get_text(strip=True) for cell in cells]

    del players[1::2]  # removing odd elements of the list

    # removing (TW), (C), (TW, FA), (FA) and (L) after players' name
    pattern = r'(\(TW\))|(\(C\))|(\(TW, FA\))|(\(FA\))|(\(L\))'
    players = [re.sub(pattern=pattern, repl='', string=player)
               for player in players]

    players_urls = ['https://en.wikipedia.org' + table.find_all(
        name='a', text=player)[0]['href'] for player in players]

    return players, players_urls


def extract_players_stats(player_url):
    """
    Function to extract the stats of a player.

    :param player_url: str: Website to be scrapped.

    :return players_urls: dict: Containing RPG, BPG, PPG of a player.
    """
    request = req.get(player_url)
    assert request.status_code == 200

    # parsing html to bs4
    website = BeautifulSoup(request.content, 'lxml')

    table = website.find(name='table',
                         attrs={'class': 'wikitable sortable',
                                'style': 'text-align:right;'})

    try:
        cells = table.find_all(name='tr')

        if cells[-1].text.find('Career') == 1:
            if '2019–20' == cells[-2].get_text(strip=True)[:7]:
                cols = cells[-2].find_all(name='td')
                return {'RPG': float(cols[-5].get_text(strip=True)),
                        'BPG': float(cols[-2].get_text(strip=True)),
                        'PPG': float(cols[-1].get_text(strip=True))}
            else:
                return {'RPG': 0., 'BPG': 0., 'PPG': 0.}

        elif cells[-1].text.find('All-Star') == 1:
            if '2019–20' == cells[-3].get_text(strip=True)[:7]:
                cols = cells[-3].find_all(name='td')
                return {'RPG': float(cols[-5].get_text(strip=True)),
                        'BPG': float(cols[-2].get_text(strip=True)),
                        'PPG': float(cols[-1].get_text(strip=True))}
            else:
                return {'RPG': 0., 'BPG': 0., 'PPG': 0.}

        elif '2019-20' == str(cells[-1].get_text(strip=True)[:7]):
            cols = cells[-1].find_all(name='td')
            return {'RPG': float(cols[-5].get_text(strip=True)),
                    'BPG': float(cols[-2].get_text(strip=True)),
                    'PPG': float(cols[-1].get_text(strip=True))}

        else:
            return {'RPG': 0., 'BPG': 0., 'PPG': 0.}

    except:
        return {'RPG': 0., 'BPG': 0., 'PPG': 0.}


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/2020_NBA_playoffs'

    # scrapping teams in semifinals and its' urls
    teams_in_semifinals, teams_url = extract_url_teams(url)

    # dictionary comprehension to group team/player/url
    team_players = {team: '' for team in teams_in_semifinals}

    # scrapping players and its' urls for each team
    for team, team_url in zip(teams_in_semifinals, teams_url):
        players, players_urls = extract_url_players(team_url)

        p = {player: player_url for player, player_url
             in zip(players, players_urls)}

        team_players[f'{team}'] = p

    # scrapping stats by players and teams
    # grouping team/player/stats in team_players dict
    for team, players in team_players.items():
        for player, url in players.items():
            stats = extract_players_stats(player_url=url)
            team_players[f'{team}'][f'{player}'] = stats

    # cleaning memory
    del p, player, players, players_urls, stats, team, team_url, \
        teams_in_semifinals, teams_url, url

    # plotting and saving top3 for RPG, BPG, PPG for each team
    lables = ['RPG', 'BPG', 'PPG']
    titles = ['Rebounds per game', 'Blocks per game', 'Points per game']
    saves = ['NBA_player_statistics/players_over_rpg.png',
             'NBA_player_statistics/players_over_bpg.png',
             'NBA_player_statistics/players_over_ppg.png']

    for l, t, s in zip(lables, titles, saves):
        df_plot = None
        for team, player in team_players.items():
            if team == 'Milwaukee':
                df = pd.DataFrame(team_players[f'{team}']).transpose()
                a = df[f'{l}'].nlargest(3)
                a = a.to_frame()
                a['Team'] = [f'{team}'] * 3
                a['Player'] = a.index
                a.set_index(['Team', 'Player'], inplace=True)
                df_plot = a
            else:
                df = pd.DataFrame(team_players[f'{team}']).transpose()
                a = df[f'{l}'].nlargest(3)
                a = a.to_frame()
                a['Team'] = [f'{team}'] * 3
                a['Player'] = a.index
                a.set_index(['Team', 'Player'], inplace=True)
                df_plot = pd.concat([df_plot, a])

        # comparing and plotting the stats
        sns.catplot(kind="bar", data=df_plot.transpose())
        plt.title(f'{t}')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(f'{s}')
        # plt.show()
