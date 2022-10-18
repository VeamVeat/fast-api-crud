import json

from starlette import status

from dependencies import settings


class TestBook:
    def test_create_book(self, client, data_create_book):
        response = client.post("/book/", json.dumps(data_create_book))

        assert response.status_code == status.HTTP_201_CREATED

    def test_get_book_by_id(self, client, create_book):
        response = client.get("/book/1")
        content = json.loads(response.content)

        assert response.status_code == status.HTTP_200_OK
        assert content.get("id") == 1
        assert content.get("title") == settings.TEST_TITLE_BOOK
        assert content.get("rating") == settings.TEST_RATING_BOOK

    def test_get_books(self, client, create_book):
        response = client.get("/book/all")
        content = json.loads(response.content)

        assert response.status_code == status.HTTP_200_OK
        assert len(content) == 1
        assert content[0].get("id") == 1
        assert content[0].get("title") == settings.TEST_TITLE_BOOK
        assert content[0].get("rating") == settings.TEST_RATING_BOOK

    def test_update_book_by_id(self, client, create_book):
        data = {
            "title": settings.TEST_UPDATE_TITLE_BOOK,
            "rating": settings.TEST_UPDATE_RATING_BOOK
        }
        response = client.put("/book/1", json.dumps(data))
        content = json.loads(response.content)

        assert response.status_code == status.HTTP_200_OK
        assert content.get("id") == 1
        assert content.get("title") == settings.TEST_UPDATE_TITLE_BOOK
        assert content.get("rating") == settings.TEST_UPDATE_RATING_BOOK

    def test_optional_update_book_by_id(self, client, create_book):
        data = {
            "title": settings.TEST_UPDATE_TITLE_BOOK
        }
        response = client.patch("/book/1", json.dumps(data))
        content = json.loads(response.content)

        assert response.status_code == status.HTTP_200_OK
        assert content.get("id") == 1
        assert content.get("title") == settings.TEST_UPDATE_TITLE_BOOK
        assert content.get("rating") == settings.TEST_RATING_BOOK

    def test_delete_book_by_id(self, client, create_book):
        response = client.delete(f"/book/1")

        assert response.status_code == status.HTTP_200_OK
