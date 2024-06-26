from flask import request, jsonify
from config import app, db
from models import Contact, Game
from sqlalchemy import func

@app.route('/')
def main():
    # Start the Data Base if it's not already created
    with app.app_context():
        db.create_all()

    return app.send_static_file('index.html')


@app.route("/home_games", methods=["GET"])
def get_all_games():
    games = Game.query.all()
    json_games = list(map(lambda x: x.to_json(), games))

    return jsonify({"games": json_games})

@app.route("/game/<int:game_id>", methods=["GET"])
def get_game(game_id):
    game = Game.query.get(game_id)

    if not game:
        return jsonify({"message": "Game not found"}), 404

    return jsonify({"game": game.to_json()})

@app.route("/search/<query>", methods=["GET"])
def search_game(query):
    games = Game.query.filter(Game.title.like('%' + query + '%'))
    json_games = list(map(lambda x: x.to_json(), games))

    return jsonify({"games": json_games})

@app.route("/teaser/<src>", methods=["GET"])
def get_img(src):
    print("Sending: " + src)
    return app.send_static_file(src)


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))

    return jsonify({"contacts": json_contacts})


@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must fill all the required fields"}), 400

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created successfully"}), 201


@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated successfully!"}), 200


@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted successfully!"}), 200


# Local test
if __name__ == "__main__":
    # Create all tables (CREATE IF NOT EXISTS)
    with app.app_context():
        db.create_all()

    app.run(debug=True)