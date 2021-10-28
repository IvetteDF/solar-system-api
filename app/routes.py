from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.moons,
            })
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"], description=request_body["description"], moons=request_body["moons"])

        db.session.add(new_planet)
        db.session.commit()

        return jsonify(f"Planet {new_planet.name} was successfully created"), 201

@planets_bp.route("/<id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(id):
    planet = Planet.query.get(id)
    if planet is None:
        return jsonify(f"Error: Planet #{id} not found"), 404
        
    if request.method == "GET":
        return {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "moons" : planet.moons,
            }
    elif request.method == "PUT":
        request_body = request.get_json()

        planet.name = request_body["name"]
        planet.description = request_body["description"]
        planet.moons = request_body["moons"]

        db.session.commit()

        return jsonify(f"Planet {planet.name} successfully updated!"), 200
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()

        return jsonify(f"Planet {planet.name} successfully deleted!"), 200



# def get_response(planet):
#     path = "https://api.le-systeme-solaire.net/rest/bodies/"

#     query_params = {
#     "filter[]" : f"englishName,eq,{planet}"
#     }

#     response = requests.get(path, params=query_params).json()
#     print(response)
#     print()

# get_response("mars")
# get_response("venus")
