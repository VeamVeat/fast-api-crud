import json

from starlette import status

from dependencies import settings


def test_create_author(client, data_create_author):
    response = client.post("/author/", json.dumps(data_create_author))

    assert response.status_code == status.HTTP_201_CREATED


def test_get_author_by_id(client, create_author):
    response = client.get("/author/1")
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert content.get("id") == 1
    assert content.get("name") == settings.TEST_NAME_AUTHOR
    assert content.get("age") == settings.TEST_AGE_AUTHOR


def test_get_authors(client, create_author):
    response = client.get("/author/all")
    content = json.loads(response.content)

    assert len(content) == 1
    assert response.status_code == status.HTTP_200_OK
    assert content[0].get("id") == 1
    assert content[0].get("name") == settings.TEST_NAME_AUTHOR
    assert content[0].get("age") == settings.TEST_AGE_AUTHOR


def test_update_author(client, create_author):
    data = {
        "name": settings.TEST_UPDATE_NAME_AUTHOR,
        "age": settings.TEST_UPDATE_AGE_AUTHOR
    }
    response = client.put("/author/1", json.dumps(data))
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert content.get("id") == 1
    assert content.get("name") == 'Ivan'
    assert content.get("age") == 22


def test_optional_update_author_by_id(client, create_author):
    data = {
        "age": settings.TEST_UPDATE_AGE_AUTHOR
    }
    response = client.patch("/author/1", json.dumps(data))
    content = json.loads(response.content)

    assert response.status_code == status.HTTP_200_OK
    assert content.get("id") == 1
    assert content.get("name") == settings.TEST_NAME_AUTHOR
    assert content.get("age") == settings.TEST_UPDATE_AGE_AUTHOR


def test_add_book_to_author_id(client, create_author, create_book):
    data = {"book_id": 1}
    response = client.post("/author/1", json.dumps(data))
    content = json.loads(response.content)
    books = content.get("books")[0]

    assert response.status_code == status.HTTP_200_OK
    assert content.get("id") == 1
    assert content.get("name") == settings.TEST_NAME_AUTHOR
    assert content.get("age") == settings.TEST_AGE_AUTHOR
    assert books.get("id") == 1
    assert books.get("title") == settings.TEST_TITLE_BOOK
    assert books.get("rating") == settings.TEST_RATING_BOOK


def test_delete_author_by_id(client, create_author):
    b = create_author
    author_id = settings.TEST_AUTHOR_ID
    response = client.delete(f"/author/{author_id}")

    assert response.status_code == status.HTTP_200_OK
