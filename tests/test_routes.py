# from flask.wrappers import Response

# ^ huh ?? why was this in my hello books code ? 

def test_get_planet_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name" : "venus",
        "description" : "hottie w a body",
        "moons" : 0
    }

def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == "Error: Planet #1 not found"

def test_get_all_planets(client, two_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [
        {
        "id" : 1,
        "name" : "venus",
        "description" : "hottie w a body",
        "moons" : 0
    },
    {
        "id" : 2,
        "name" : "earth",
        "description" : "in her flop era",
        "moons" : 1
    }
    ]

def test_create_a_planet_when_none_exists(client):
    response = client.post("/planets", json={"name" : "mars", "description" : "future mall of america", "moons" : 0})
    response_body = response.get_json()


    assert response.status_code == 201
    assert response_body == "Planet mars was successfully created"

