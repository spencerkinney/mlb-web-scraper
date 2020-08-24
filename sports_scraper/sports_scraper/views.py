from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup

def hitters(request):
    url = 'https://www.mlb.com/stats/hitting'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'lxml')

    players_parser = soup.find_all(class_="short-3OJ0bTju")
    positions_parser = soup.find_all(class_="position-28TbwVOg")
    teams_parser = soup.find_all(class_="col-group-end-2UJpJVwW number-aY5arzrB align-left-3L2SU-Mk is-table-pinned-1WfPW2jT")

    players_attr = {
        "name": [],
        "position": [],
        "team": []
    }

    #Iterates through web page and stores every instance of parsed HTML classes
    for player in players_parser:
        players_attr["name"].append(str(player.text))
    for position in positions_parser:
        players_attr["position"].append(str(position.text))
    for team in teams_parser:
        players_attr["team"].append(str(team.text))

    # Iterates through the player_attr dictionary items and creates a new 'players_sub_list' for each player inside the 'player_list'
    players_list = []
    players_sublist = []

    for i in range(len(players_attr["name"])):
        players_sublist = []
        players_sublist.append(str(i +1))
        players_sublist.append(players_attr["name"][i])
        players_sublist.append(players_attr["position"][i])
        players_sublist.append(players_attr["team"][i])
        players_list.append(players_sublist)


    '''

    INPUT:   print(players_list)

    EXAMPLE OUTPUT:   [['1', 'N Cruz', 'DH', 'MIN'], ['2', 'B Harper', 'RF', 'PHI'], ['3', 'L Voit', '1B', 'NYY'], ['4', 'B Lowe', '2B', 'TB'], ['5', 'J Winker', 'DH', 'CIN'], ['6', 'M Yastrzemski', 'CF', 'SF'], ['7', 'F Tatis Jr.', 'SS', 'SD'], ['8', 'K Lewis', 'CF', 'SEA'], ['9', 'R Grossman', 'LF', 'OAK'], ['10', 'J Abreu', '1B', 'CWS'], ['11', 'M Betts', 'RF', 'LAD'], ['12', 'A Rendon', '3B', 'LAA'], ['13', 'C Blackmon', 'RF', 'COL'], ['14', 'I Happ', 'CF', 'CHC'], ['15', 'A Santander', 'RF', 'BAL'], ['16', 'T Hernández', 'RF', 'TOR'], ['17', 'D LeMahieu', '2B', 'NYY'], ['18', 'P Severino', 'C', 'BAL'], ['19', 'P Goldschmidt', '1B', 'STL'], ['20', 'F Freeman', '1B', 'ATL'], ['21', 'J Realmuto', 'C', 'PHI'], ['22', 'M Trout', 'CF', 'LAA'], ['23', 'T Turner', 'SS', 'WSH'], ['24', 'N Castellanos', 'RF', 'CIN'], ['25', 'T Story', 'SS', 'COL']]

    '''


    return render(request, 'index.html', {'players_list': players_list})

def index(request):
    return render (request, 'index.html')

