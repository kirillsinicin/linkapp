def test_index(client):
    response = client.get("links/")
    assert b"Hello links" in response.data


def test_links_create(client, user):
    response = client.post(
        "links/create",
        data={"name": "yandex", "destination": "https://ya.ru/"},
        headers={f"Authorization": f"Bearer {user.id}"},
    )
    assert response.status_code == 200


def test_links_create_un_auth(client):
    response = client.post(
        "links/create",
        data={"name": "yandex", "destination": "https://ya.ru/"},
        headers={f"Authorization": f"Bearer un_auth_user"},
    )
    assert response.status_code == 401


def test_redirect_to_original_link(client, link):
    response = client.get(f"links/{link.short_link}")
    expected_original_link = f"{link.original_link}"
    assert response.status_code == 302
    assert response.headers["Location"] == expected_original_link
