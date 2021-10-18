from flask import Blueprint, jsonify
import requests

class Planet:
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet(1, "Mercury", "Rogue moon turned planet!", 0),
    Planet(2, "Venus", "Hottest planet in our solar system ;-)", 0),
    Planet(3, "Earth", "In her flop era", 1)
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {"id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "moons" : planet.moons,
            }
        )

    return jsonify(planets_response)

@planets_bp.route("/<id>", methods=["GET"])
def handle_planet(id):
    id = int(id)
    for planet in planets:
        if planet.id == id:
            return {
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "moons" : planet.moons,
                }

def get_response(planet):
    path = "https://api.le-systeme-solaire.net/rest/bodies/"

    query_params = {
    "filter[]" : f"englishName,eq,{planet}"
    }

    response = requests.get(path, params=query_params).json()
    print(response)
    print()

get_response("mars")
get_response("venus")
