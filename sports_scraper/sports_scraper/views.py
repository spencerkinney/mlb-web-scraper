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
    gamesplayed_parser = soup.find_all(attrs={"data-col" : "2"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
    atbats_parser = soup.find_all(attrs={"data-col" : "3"}, class_="col-group-end-2UJpJVwW number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
    runs_parser = soup.find_all(attrs={"data-col" : "4"}, class_="col-group-start-sa9unvY0 number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")
    hits_parser = soup.find_all(attrs={"data-col" : "5"}, class_="number-aY5arzrB align-right-3nN_D3xs is-table-pinned-1WfPW2jT")

    # Creates a list of attributes for each player ('players_sub_list') for each player and stores it in the 'player_list' list
    players_list = []
    players_sublist = []
    playerCount = len(players_parser)

    for i in range(playerCount):
        players_sublist = []
        players_sublist.append(i +1)
        players_sublist.append(str(players_parser[i].text))
        players_sublist.append(str(positions_parser[i].text))
        players_sublist.append(str(teams_parser[i].text))
        players_sublist.append(str(gamesplayed_parser[i].text))
        players_sublist.append(str(atbats_parser[i].text))
        players_sublist.append(str(runs_parser[i].text))
        players_sublist.append(str(hits_parser[i].text))
        players_list.append(players_sublist)
    
    '''

    INPUT:   print(players_list)

    EXAMPLE OUTPUT: [[1, 'L Voit', '1B', 'NYY', '23', '80', '17', '24'], [2, 'B Harper', 'RF', 'PHI', '25', '82', '23', '26'], [3, 'B Lowe', '2B', 'TB', '31', '107', '26', '32'], [4, 'N Cruz', 'DH', 'MIN', '31', '110', '23', '35'], [5, 'J Abreu', '1B', 'CWS', '31', '125', '23', '40']...

    '''

    return render(request, 'index.html', {'players_list': players_list})

def index(request):
    return render (request, 'index.html')

