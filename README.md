<h1>Yatube_api</h1>
<h3>Применяемые технологии.</h3>
    В данном проекте основным языком программирования является Python. Используемый фреймворк: Django. Помимо этого для реализации JWT-аутентификации использовалась библиотека djoser 2.1.0 
<h3>Описание.</h3>
    Проект представляет собой блог-сервис, который предполагает возможность зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора, а так же подписаться на обновления авторов.
<h3>Установка.</h3>
    Для установки требуется кланировать проект командой: git clone <Ссылка_на_проект>.
    Далее создайте: _py -m venv venv_
    и активируйте виртуальное окружение: _source venv/Scripts/activate _
    установите все необходимые пакеты:_ pip install -r requirements.txt_
    После этого проект готов к запуску.
<h3>Примеры. Некоторые примеры запросов к API.</h3>
    http://127.0.0.1:8000/api/v1/posts/ - запрос для получения/создания(в зависимости от типа запроса) постов
    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - то же самое, но с комментариями
    http://127.0.0.1:8000/api/v1/follow/ - подписки
    http://127.0.0.1:8000/api/v1/jwt/create/ - получение JWT-токена
<h3>Автор проекта.</h3> CaSSiDYFox@yandex.ru
