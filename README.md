> API crud

---

## Оглавление
* [Общее](#общее)
* [Используемые языки и фреймворки](#используемые-языки-и-фреймворки)
* [Используемые технологии](#используемые-технологие)
* [Используемые базы данных](#используемые-базы-данных)
* [Функции API](#функции-api)
* [Настройка и запуск проекта](#настройка-и-запуск-проекта)

## Общее
- API для crud операций

## Используемые языки и фреймворки
- Python 3.10
- Fastapi==0.85.0
- Pydantic==1.10.2
- SQLAlchemy==1.4.41
- Alembic==1.8.1

## Используемые базы данных
- PostgreSQL 2.9.3

## Функции API
- http://0.0.0.0:8000/author/all -> получить всех авторов (get)
- http://0.0.0.0:8000/author/{author_id} -> получить автора по id (get)
- http://0.0.0.0:8000/author/{author_id} -> обновить все данные об авторе (put)
- http://0.0.0.0:8000/author/{author_id} -> добавить id книги автору по его id (post)
- http://0.0.0.0:8000/author/{author_id} -> удалить автора по id (delete)
- http://0.0.0.0:8000/author/{author_id} -> частично изменить данные об авторе (patch)
- http://0.0.0.0:8000/author/-> создать нового автора (post)
- 
- http://0.0.0.0:8000/book/all -> получить все книги (get)
- http://0.0.0.0:8000/book/{book_id} -> получить книгу по id (get)
- http://0.0.0.0:8000/book/{book_id} -> обновить все данные о книги (put)
- http://0.0.0.0:8000/book/{book_id} -> удалить книгу по id (delete)
- http://0.0.0.0:8000/book/{book_id} -> частично изменить данные о книге (patch)
- http://0.0.0.0:8000/book/ -> создать новую книгу (post)

## Настройка и запуск проекта
Для начала склонируйте репозиторий и установить зависимости

`git clone https://github.com/VeamVeat/fast_api_crud.git`

```Python
python3.10 -m venv env
cd env/bin
source activate
cd ../.. && cd fast_api_crud
pip install -r requirements.txt
alembic upgrade head
```

#### Для локального запуска
`uvicorn main:app --reload`
