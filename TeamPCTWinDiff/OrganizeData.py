
team_diffs = {}
for year in range(2001, 2021):
    f = open(f'./Team_Data/TeamPCTWinDiff_{year}.txt', 'r')
    lines = f.readlines()
    f.close()

    data = []
    for line in lines:
        data.append(line.strip('\n()').split(','))
    for team, diff in data:
        if (not team_diffs.get(team, False)):
            team_diffs[team] = []
        team_diffs[team].append(f'({year}) {diff}')

f = open(f'./Team_Data/TeamPCTWinDiffOverTime.txt', 'w')
for team in team_diffs:
    print(f'{team},{team_diffs[team]}', file=f)
