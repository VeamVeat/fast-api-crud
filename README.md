> API crud

---

## Оглавление
* [Общее](#общее)
* [Используемые языки и фреймворки](#используемые-языки-и-фреймворки)
* [Используемые базы данных](#используемые-базы-данных)
* [Функции API](#функции-api)
* [Настройка и запуск проекта на локальной машине](#настройка-и-запуск-проекта-на-локальной-машине)
* [Настройка и запуск проекта в докер контейнере](#настройка-и-запуск-проекта-в-докер-контейнере)

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
- http://0.0.0.0:8000/authors/ -> получить всех авторов (get)
- http://0.0.0.0:8000/authors/-> создать нового автора (post)
- http://0.0.0.0:8000/authors/{author_id} -> получить автора по id (get)
- http://0.0.0.0:8000/authors/{author_id} -> обновить все данные об авторе (put)
- http://0.0.0.0:8000/authors/{author_id} -> добавить id книги автору по его id (post)
- http://0.0.0.0:8000/authors/{author_id} -> удалить автора по id (delete)
- http://0.0.0.0:8000/authors/{author_id} -> частично изменить данные об авторе (patch)


- http://0.0.0.0:8000/books/ -> получить все книги (get)
- http://0.0.0.0:8000/books/ -> создать новую книгу (post)
- http://0.0.0.0:8000/books/{book_id} -> получить книгу по id (get)
- http://0.0.0.0:8000/books/{book_id} -> обновить все данные о книги (put)
- http://0.0.0.0:8000/books/{book_id} -> удалить книгу по id (delete)
- http://0.0.0.0:8000/books/{book_id} -> частично изменить данные о книге (patch)

## Настройка и запуск проекта на локальной машине
Для начала склонируйте репозиторий и установить зависимости

`git clone https://github.com/VeamVeat/fast_api_crud.git`

```Python
python3.10 -m venv env
cd env/bin
source activate
cd ../.. && cd fast_api_crud
pip install -r requirements.txt

sudo -u postgres psql
create database fast_api_crud;
create user username with encrypted password 'password';
grant all privileges on database fast_api_crud to username;

alembic upgrade head
pytest (удостовериться что все тесты прошли успешно)
```
![Снимок экрана от 2022-10-22 15-09-23](https://user-images.githubusercontent.com/67123448/197338305-23148b3e-9e2e-465e-ae90-7ce3cea84151.png)
 
```
`uvicorn main:app --reload`
```

## Настройка и запуск проекта в докер контейнере
Для начала склонируйте репозиторий и установить зависимости

`git clone https://github.com/VeamVeat/fast_api_crud.git`

```Python
python3.10 -m venv env
cd env/bin
source activate
cd ../.. && cd fast_api_crud
pip install -r requirements.txt

make setup

#В отдельном терминале 
cd fast_api_crud (зайти в папку с проектом)
make login
alembic upgrade head
pytest (удостовериться что все тесты прошли успешно)
```
![Снимок экрана от 2022-10-22 14-49-47](https://user-images.githubusercontent.com/67123448/197338206-3eb444ea-54b2-4273-b1d4-4c755d3eef4c.png)
