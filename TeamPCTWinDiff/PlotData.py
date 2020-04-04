import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

f = open('./Team_Data/TeamPCTWinDiffOverTime.txt', 'r')
lines = f.readlines()

df = pd.DataFrame()
plotted_line = []
fig = go.Figure()

for i, line in enumerate(lines):
    split_line = line.split(',')
    team = split_line[0].strip('\'')
    temp_team = []
    for word in team.split(): temp_team.append(word.lower().capitalize())
    team = ' '.join(temp_team)
    data = split_line[1:]
    team_data=[]
    years=[]
    for point in data:
        coords = point.split(' ')
        while("" in coords) :
            coords.remove("")
        stripped_coords = []
        for c in coords:
            stripped_coords.append(c.strip('()[]\n\' '))
        years.append(int(stripped_coords[0]))
        team_data.append(float(stripped_coords[1]))
    if i == 0: df['Years'] = years
    df[team] = pd.Series(team_data)
    fig.add_scatter(x=df['Years'],
    y=df[team],
    mode='lines+markers',
    name=team)
print(df)
fig.show()

#     plt.plot(x, y, label=team)
# plt.legend()
# plt.show()
