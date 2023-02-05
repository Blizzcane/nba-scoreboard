# NBA Game Scoreboard
This is a Flask-based web server that displays the latest scores of NBA games. The scores are fetched from the nba_api and are updated every minute.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have flask and nba_api installed in your python environment. You can install them by running:

```
pip install flask nba_api
```

### Running the Server
Clone the repository and navigate to the project directory. Then run the following command to start the server:

```
flask --app nba run
```
The server will start at http://127.0.0.1:5000/ by default.

## Built With
- Flask - The web framework used
- nba_api - API for NBA data 
