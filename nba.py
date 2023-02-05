from flask import Flask 
from nba_api.live.nba.endpoints import scoreboard

# Today's Score Board
games = scoreboard.ScoreBoard()

gameData = games.get_json()

print(gameData)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"