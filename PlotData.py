import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
f = open('./Team_Data/TeamPCTWinDiffOverTime.txt', 'r')
lines = f.readlines()

df = pd.DataFrame()
for line in lines[:4]:
    split_line = line.split(',')
    team = split_line[0]
    data = split_line[1:]
    x=[]
    y=[]
    for point in data:
        coords = point.split(' ')
        while("" in coords) :
            coords.remove("")
        stripped_coords = []
        for c in coords:
            stripped_coords.append(c.strip('()[]\n\' '))
        x.append(int(stripped_coords[0]))
        y.append(float(stripped_coords[1]))

    plt.plot(x, y, label=team)
plt.legend()
plt.show()

#     df = df.append({team : x, 'Percent Point Diff' : y}, ignore_index=True)
#     fig = px.line(df, x=team, y="Percent Point Diff", title='Percent Point Differential by Team')
# fig.show()
