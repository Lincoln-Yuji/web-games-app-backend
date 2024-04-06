from config import app, db
from models import Game

def create_games(game_list):
    for game in game_list:
        if not game["title"] or not game["url"]:
            continue

        new_game = Game(title=game["title"], url=game["url"])

        try:
            db.session.add(new_game)
        except Exception as e:
            print("Error: " + str(e))
            print("Error while trying to add " + new_game.title)
            print("===========================================")

    try:
        db.session.commit()
    except Exception as e:
        print("Error: " + str(e))
        print("Error while commiting changes...")


if __name__ == "__main__":
    with app.app_context():
        games =[
            {
                "title": "Cut the Rope",
                "url": "https://play.famobi.com/wrapper/cut-the-rope"
            },
            {
                "title": "Cursed Marbles",
                "url": "https://play.famobi.com/totemia-cursed-marbles"
            }
        ]
        create_games(games)