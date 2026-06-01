from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random




app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(
        db.select(Cafe)
    ).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(
        cafe={
            "id": random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }
    )

@app.route("/all")
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()

    all_cafes = []

    for cafe in cafes:
        all_cafes.append({
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        })

    return jsonify(cafes=all_cafes)

@app.route("/search")
def search():
    loc = request.args.get("loc")
    cafe = db.session.execute(
        db.select(Cafe).where(Cafe.location == loc)
    ).scalar()

    if cafe:
        return jsonify(
            cafe={
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            }
        )
    return jsonify(
        error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        }
    )

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
    name=request.form.get("name"),
    map_url=request.form.get("map_url"),
    img_url=request.form.get("img_url"),
    location=request.form.get("location"),
    seats=request.form.get("seats"),
    has_toilet=bool(request.form.get("has_toilet")),
    has_wifi=bool(request.form.get("has_wifi")),
    has_sockets=bool(request.form.get("has_sockets")),
    can_take_calls=bool(int(request.form.get("can_take_calls"))),
    coffee_price=request.form.get("coffee_price"),
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(
        response={
            "success": "Successfully added the new cafe."
        }
    )

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):

    new_price = request.args.get("new_price")

    cafe = db.session.get(Cafe, cafe_id)

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(
            success="Successfully updated the price."
        )

    return jsonify(
        error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        }
    ), 404

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):

    api_key = request.args.get("api-key")

    if api_key != "TopSecretAPIKey":
        return jsonify(
            error="Sorry, that's not allowed. Make sure you have the correct api_key."
        ), 403

    cafe = db.session.get(Cafe, cafe_id)

    if not cafe:
        return jsonify(
            error={
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        ), 404

    db.session.delete(cafe)
    db.session.commit()

    return jsonify(
        response={
            "success": "Successfully deleted the cafe."
        }
    )


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
