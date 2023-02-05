from flask import Flask 
from nba_api.live.nba.endpoints import scoreboard

# Query nba.live.endpoints.scoreboard and  list games in localTimeZone
from datetime import datetime, timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard, boxscore

# f = "{awayTeam} vs. {homeTeam}" 

# board = scoreboard.ScoreBoard()
# print("ScoreBoardDate: " + board.score_board_date)
# games = board.games.get_dict()
# for game in games:
#     print("")
#     print(f.format(gameId=game['gameId'], awayTeam=game['awayTeam']['teamName'], homeTeam=game['homeTeam']['teamName']))
#     box = boxscore.BoxScore(game['gameId']) 
#     currentScore = "{homeScore} - {awayScore}"
    
#     print(currentScore.format(homeScore=box.get_dict()['game']['homeTeam']['score'],awayScore=box.get_dict()['game']['awayTeam']['score']))
#     print(game['gameStatusText'])
    
 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"