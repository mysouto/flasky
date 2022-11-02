def test_get_all_bikes_with_empty_db_returns_empty_list(client):
    # can use client.request_method => client.get, client.post
    response = client.get("/bike")
    response_body = response.get_json()

    # run assertions to test response
    assert response_body == []
    assert response.status_code == 200


# empty database returns 404 error
def test_get_one_bike_with_empty_db_returns_404(client):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert "message" in response_body
    assert response.status_code == 404


# import client + fixture name
def test_get_one_bike_with_populated_db_returns_bike_json(client, two_bikes):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Speedy",
        "price": 10,
        "size": 30,
        "type": "hybrid"
    }
