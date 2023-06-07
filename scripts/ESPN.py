import requests
import os
import sys

"""
This script scrapes data from an ESPN game play-by-play log and outputs in a .csv file of the form:

Year_Month_Day_ESPNGameID_Home_Away.csv

For example, the Miami Heat visited the Portland Trailblazers on December 28th, 2013.
The corresponding file would be titled:

2013_12_28_400489319_POR_MIA.csv

"""

def scrape_test_game():
    gameID = 400489319


    print("Requesting the page:")
    r = requests.get('https://www.espn.com/nba/playbyplay/_/gameId/%d' % gameID)
    assert r != 200, "Not able to access the page!"

    html_page = r.text

    print(html_page)


if __name__ == "__main__":
    #scrape_test_game()
    print(os.path.dirname(sys.executable))






























































































