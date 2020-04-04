
player_years = {}
for year in range(2000, 2021):
    f = open(f"./SeasonData/{year}_totals.CSV")
    flines = f.readlines()
    f.close()
    for line in flines[1:]:
        player_year = line.rstrip('\n').split(',')
        name = player_year[1]
        fgm = int(player_year[8])
        threepm = int(player_year[10])
        twopm = fgm-threepm
        ftm = int(player_year[12])
        points = 3*threepm + 2*twopm + ftm
        label = f"{name}-{year}"
        if (player_years.get(label, False)):
            player_years[label] += points
        else:
            player_years[label] = points
