import numpy as np
import pandas as pd
import json

matches=pd.read_csv('flask/ApI_development/ipl-matches.csv')

def teamAPI():
     teams= list(set(list(matches['Team1'])+list(matches['Team2'])))
     teams_dict={
          'teams':teams
     }
     return teams_dict
def teamvteamAPI(team1,team2):
    valid_team=teamAPI()
    if team1 in valid_team['teams'] and team2 in valid_team['teams']:
         team_df=matches[(matches['Team1']==team1) & (matches['Team2']==team2) | (matches['Team1']==team2) & (matches['Team2']==team1)]
         total_matches=team_df.shape[0]

         matches_won_team1=team_df['WinningTeam'].value_counts().get(team1,0)
         matches_won_team2=team_df['WinningTeam'].value_counts().get(team2,0)
         draws=total_matches-(matches_won_team1+matches_won_team2)
         response={
             'total_matches':str(total_matches),
             team1:str(matches_won_team1),
             team2:str(matches_won_team2),
             'draw':str(draws)

          }
         return response
    else:
         return {'message':'invalid team name'}
