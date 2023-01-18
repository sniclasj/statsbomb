import pandas
from statsbombpy import sb

df = sb.competitions()

# df.to_csv('comps.csv', index=False)

df_comp_16 = df[df['competition_id'] == 16]

df_comp_16_season_4 = df_comp_16[df_comp_16['season_id'] == 4]
# print(df_comp_16_season_4)
# df_comp_16_season_4.to_csv('season4.csv', index=False)

match = sb.matches(16, 4)
# print(match)

# match.to_csv('match.csv', index=False)

livtot = sb.events(22912)
print(livtot)
