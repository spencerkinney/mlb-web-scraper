import requests
from bs4 import BeautifulSoup

def get_hitters_information(url):
    hitters_list = []
    hitters_sublist = []

    # Iterate through each /stats/hitting/?page=X
    for page in range(1, 8):
        reqs = requests.get(url + '/?page=' + str(page))
        soup = BeautifulSoup(reqs.text, 'lxml')

        # Get all relevant column data
        hitters_parser = soup.find_all(class_="short-3OJ0bTju")
        positions_parser = soup.find_all(class_="position-28TbwVOg")
        teams_parser = soup.find_all(class_="col-group-end-2UJpJVwW number-aY5arzrB align-left-3L2SU-Mk is-table-pinned-1WfPW2jT")
        gamesplayed_parser = soup.find_all(attrs={"data-col" : "2"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        atbats_parser = soup.find_all(attrs={"data-col" : "3"}, class_="col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        runs_parser = soup.find_all(attrs={"data-col" : "4"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        hits_parser = soup.find_all(attrs={"data-col" : "5"}, class_="number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")

        '''
        Iterate through each list, appending each to a sublist that represents each player, and then append the player sublist
        to a list of all hitters.
        '''
        hittersCount = len(hitters_parser)
        for i in range(hittersCount):
            hitters_sublist = []
            hitters_sublist.append( i + 1 + 25 * (page - 1) )
            hitters_sublist.append(str(hitters_parser[i].text))
            hitters_sublist.append(str(positions_parser[i].text))
            hitters_sublist.append(str(teams_parser[i].text))
            hitters_sublist.append(str(gamesplayed_parser[i].text))
            hitters_sublist.append(str(atbats_parser[i].text))
            hitters_sublist.append(str(runs_parser[i].text))
            hitters_sublist.append(str(hits_parser[i].text))
            hitters_list.append(hitters_sublist)
    
    # Create a list of all the unique teams of the hitters
    teams_list = []
    for hitter in hitters_list:
        if hitter[3] not in teams_list:
            teams_list.append(hitter[3])

    # Create a roster of hitters where each key is a team and each value is a list of player sublists that are in that team.
    '''
    roster = {}
    for team in teams_list:
        hitters_sublist = []
        for player in hitters_list:
            if player[3] == team:
                hitters_sublist.append(player)
        roster[team] = hitters_sublist
    '''
    return hitters_list
    

def get_pitchers_information(url):
    pitchers_list = []
    pitchers_sublist = []

    # Iterate through each /stats/pitching/?page=X
    for page in range(1, 3):
        reqs = requests.get(url + '/?page=' + str(page))
        soup = BeautifulSoup(reqs.text, 'lxml')

        # Get all relevant column data
        pitchers_parser = soup.find_all(class_="short-3OJ0bTju")
        positions_parser = soup.find_all(class_="position-28TbwVOg")
        teams_parser = soup.find_all(class_="col-group-end-2UJpJVwW number-aY5arzrB align-left-3L2SU-Mk is-table-pinned-1WfPW2jT")
        wins_parser = soup.find_all(attrs={"data-col" : "2"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        lose_parser = soup.find_all(attrs={"data-col" : "3"}, class_="number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
        ERA_parser = soup.find_all(attrs={"data-col" : "4"}, class_="selected-1vxxHvFg col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")

        '''
        Iterate through each list, appending each to a sublist that represents each player, and then append the player sublist
        to a list of all hitters.
        '''
        pitchersCount = len(pitchers_parser)
        for i in range(pitchersCount):
            pitchers_sublist = []
            pitchers_sublist.append( i + 1 + 25 * (page - 1) )
            pitchers_sublist.append(str(pitchers_parser[i].text))
            pitchers_sublist.append(str(positions_parser[i].text))
            pitchers_sublist.append(str(teams_parser[i].text))
            pitchers_sublist.append(str(wins_parser[i].text))
            pitchers_sublist.append(str(lose_parser[i].text))
            pitchers_sublist.append(str(ERA_parser[i].text))
            pitchers_list.append(pitchers_sublist)

    teams_list = []
    for pitcher in pitchers_list:
        # if a pitcher's team is unique append the team to a list
        if pitcher[3] not in teams_list:
            teams_list.append(pitcher[3])

    # Create a roster of pitchers where each key is a team and each value is a list of player sublists that are in that team.
    '''
    roster = {}
    for team in teams_list:
        hitters_sublist = []
        for player in hitters_list:
            if player[3] == team:
                hitters_sublist.append(player)
        roster[team] = hitters_sublist
    '''
    return pitchers_list