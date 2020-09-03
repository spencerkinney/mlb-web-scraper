import requests
from bs4 import BeautifulSoup

def get_hitters_information(url):
    players_list = []
    players_sublist = []

    # Iterate through each /stats/hitting/?page=X
    for page in range(1, 8):
        if page == 1:
            reqs = requests.get(url)
        else:
            reqs = requests.get(url + '/?page=' + str(page))
        soup = BeautifulSoup(reqs.text, 'lxml')

        # Get all relevant column data
        players_parser = soup.find_all(class_="short-3OJ0bTju")
        positions_parser = soup.find_all(class_="position-28TbwVOg")
        teams_parser = soup.find_all(class_="col-group-end-2UJpJVwW number-aY5arzrB align-left-3L2SU-Mk is-table-pinned-1WfPW2jT")
        gamesplayed_parser = soup.find_all(attrs={"data-col" : "2"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        atbats_parser = soup.find_all(attrs={"data-col" : "3"}, class_="col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        runs_parser = soup.find_all(attrs={"data-col" : "4"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        hits_parser = soup.find_all(attrs={"data-col" : "5"}, class_="number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")

        '''
        Iterate through each list, appending each to a sublist that represents each player, and then append the player to a list of
        all players.
        '''
        playerCount = len(players_parser)
        for i in range(playerCount):
            players_sublist = []
            if page == 1:
                players_sublist.append(i + 1)
            else:
                players_sublist.append(i + 1 + (25 * (page - 1)))
            players_sublist.append(str(players_parser[i].text))
            players_sublist.append(str(positions_parser[i].text))
            players_sublist.append(str(teams_parser[i].text))
            players_sublist.append(str(gamesplayed_parser[i].text))
            players_sublist.append(str(atbats_parser[i].text))
            players_sublist.append(str(runs_parser[i].text))
            players_sublist.append(str(hits_parser[i].text))
            players_list.append(players_sublist)
    
    # Create a list of all the unique teams of the hitters
    teams_list = []
    for player in players_list:
        if player[3] in teams_list:
            pass
        else:
            teams_list.append(player[3])

    # Create a roster of hitters where each key is a team and each value is a list of player lists that are in that team.
    Roster = {}
    for team in teams_list:
        players_sublist = []
        for player in players_list:
            if player[3] == team:
                players_sublist.append(player)
        Roster[team] = players_sublist
    return players_list

def get_pitchers_information(url):
    players_list = []
    players_sublist = []

    # Iterate through each /stats/pitching/?page=X
    for page in range(1, 3):
        if page == 1:
            reqs = requests.get(url)
        else:
            reqs = requests.get(url + '/?page=' + str(page))
        soup = BeautifulSoup(reqs.text, 'lxml')

        # Get all relevant column data
        players_parser = soup.find_all(class_="short-3OJ0bTju")
        positions_parser = soup.find_all(class_="position-28TbwVOg")
        teams_parser = soup.find_all(class_="col-group-end-2UJpJVwW number-aY5arzrB align-left-3L2SU-Mk is-table-pinned-1WfPW2jT")
        wins_parser = soup.find_all(attrs={"data-col" : "2"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        lose_parser = soup.find_all(attrs={"data-col" : "3"}, class_="number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        ERA_parser = soup.find_all(attrs={"data-col" : "4"}, class_="selected-1vxxHvFg col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")

        '''
        Iterate through each list, appending each to a sublist that represents each player, and then append the player to a list of
        all players.
        '''
        playerCount = len(players_parser)
        for i in range(playerCount):
            players_sublist = []
            if page == 1:
                players_sublist.append(i + 1)
            else:
                players_sublist.append(i + 1 + 25)
            players_sublist.append(str(players_parser[i].text))
            players_sublist.append(str(positions_parser[i].text))
            players_sublist.append(str(teams_parser[i].text))
            players_sublist.append(str(wins_parser[i].text))
            players_sublist.append(str(lose_parser[i].text))
            players_sublist.append(str(ERA_parser[i].text))
            players_list.append(players_sublist)

    # Create a list of all the unique teams of the pitchers
    teams_list = []
    for player in players_list:
        if player[3] in teams_list:
            pass
        else:
            teams_list.append(player[3])

    # Create a roster of pitchers where each key is a team and each value is a list of player lists that are in that team.
    Roster = {}
    for team in teams_list:
        players_sublist = []
        for player in players_list:
            if player[3] == team:
                players_sublist.append(player)
        Roster[team] = players_sublist
    return players_list