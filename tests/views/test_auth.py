def test_register_ok(client):
    response = client.post("/auth/register", data={"login": "test_login", "password": "test_password"})
    assert response.status_code == 200
    assert type(response.json) is str
    assert response.json != ""


def test_register_bad(client):
    response = client.post("/auth/register", data={"login": "test_login", "password": ""})
    assert response.status_code == 401
