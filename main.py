import requests
from bs4 import BeautifulSoup

url = "not_entered_yet"
while url == "not_entered_yet":
    user_input = input("Would you like to view the top MLB 'hitters' or 'pitchers' as of now?: ")
    if user_input == 'hitters':
        url = 'https://www.mlb.com/stats/hitting'
        print("\nTop Hitters as of now:\n")
    if user_input == 'pitchers':
        url = 'https://www.mlb.com/stats/pitching'
        print("\nTop Pitchers as of now:\n")

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

players = soup.find_all(class_="short-3OJ0bTju")
positions = soup.find_all(class_="position-28TbwVOg")
teams = soup.find_all(class_="col-group-end-2UJpJVwW number-aY5arzrB align-left-3L2SU-Mk is-table-pinned-1WfPW2jT")

index = 0

for player in players:
    player_output = (players[index].text)
    position_output = (positions[index].text)
    team_output = (teams[index].text)
    print (player_output , "|" , position_output, "for", team_output)
    index += 1