# Yatube_api
## Применяемые технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![djoser](https://img.shields.io/badge/-djoser-464646?style=flat-square)](https://djoser.readthedocs.io/en/latest/)
## Описание
Проект представляет собой блог-сервис, который предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора, а так же подписаться на обновления авторов.
## Установка
Для установки требуется кланировать проект командой: 
```
git clone <Ссылка_на_проект>
```
Далее создайте:
```
py -m venv venv
```
и активируйте виртуальное окружение:
```
source venv/Scripts/activate
```
установите все необходимые пакеты:
```
pip install -r requirements.txt
```
После этого проект готов к запуску.
### Примеры. Некоторые примеры запросов к API
http://127.0.0.1:8000/api/v1/posts/ - запрос для получения/создания(в зависимости от типа запроса) постов
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - то же самое, но с комментариями
http://127.0.0.1:8000/api/v1/follow/ - подписки
http://127.0.0.1:8000/api/v1/jwt/create/ - получение JWT-токена
## Автор проекта
[Cassiey02](https://github.com/Cassiey02/)

