from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import numpy as np
import pandas as pd

for year in range(2001, 2021):
    print(year)
    # games = client.season_schedule(
    #         season_end_year=year,
    #         output_type=OutputType.CSV,
    #         output_file_path=f"./Team_Data/{year}_results.CSV",
    #     )


    f = open(f"./Team_Data/{year}_results.CSV", "r")
    flines = f.readlines()
    f.close()
    data = []
    for line in flines[1:]:
        data.append(line.rstrip('\n').split(',')[1:])

    team_scores = {}
    for game in data:
        home_team = game[0]
        home_team_score = game[1]
        away_team = game[2]
        away_team_score = game[3]

        if (not team_scores.get(home_team, False)):
            team_scores[home_team] = {'scored': 0, 'against': 0}
        if (not team_scores.get(away_team, False)):
            team_scores[away_team] = {'scored': 0, 'against': 0}

        team_scores [home_team]['scored'] += int(home_team_score)
        team_scores [home_team]['against'] += int(away_team_score)
        team_scores [away_team]['against'] += int(home_team_score)
        team_scores [away_team]['scored'] += int(away_team_score)

    pct_point_diffs = []
    for team in team_scores:
        team_score = team_scores[team]
        pct_point_diffs.append((team, ((team_score['scored']/team_score['against']) - 1) * 100))

    pct_point_diffs = sorted(pct_point_diffs, key=lambda team: team[1], reverse=True)

    f = open(f'./Team_Data/TeamPCTWinDiff_{year}.txt', 'w')
    for team in pct_point_diffs:
        print(team, file=f)
