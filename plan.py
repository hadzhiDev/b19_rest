# 1. Что такое API?

# API — это способ, по которому одно приложение общается с другим.

# Примеры API:
# Клавиатура → компьютер (у клавиатуры есть свой API)
# Telegram бот API (команды и методы)
# Python os library (это тоже API)
# Веб-сайты → сервер (веб API)

# API — это просто набор правил:

# “Вот так ты можешь со мной взаимодействовать”.




# 2. Что такое Web API?

# Это API, доступный через Интернет, обычно по HTTP(S).

# Например:
# GET /apartments/
# POST /login/

# Возвращает JSON, XML или HTML.



# 3. Что такое REST?

# REST (Representational State Transfer) — это архитектурный стиль для создания веб-API.
# REST — не библиотека, не фреймворк, не технология.
# Это принципы, которые делают API простым, логичным, предсказуемым.


# REST говорит:

# Используй стандартные HTTP-методы:
# GET (получить данные)
# POST (создать)
# PUT/PATCH (обновить)
# DELETE (удалить)


# Каждый ресурс должен иметь URL (Uniform Resource Locator):
# /users/
# /users/10/

# Ответы обычно в JSON.

# API должен быть stateless
# (сервер не должен хранить состояние между запросами — каждый запрос независим).



# 4. Что такое REST API?

# REST API = Web API, который следует правилам REST.

# Это API, построенный:
# на HTTP,
# со стандартными методами,
# с ресурсами,
# в формате JSON.

# Пример REST API:
# GET /api/v1/apartments/ → список квартир
# POST /api/v1/apartments/ → создать квартиру
# GET /api/v1/apartments/5/ → квартира с id=5
# PUT /api/v1/apartments/5/ → обновить квартиру
# DELETE /api/v1/apartments/5/ → удалить квартиру

# Запросы — это действия,
# URL — это ресурсы,
# JSON — это данные.




# API — это способ, как программы общаются между собой.
# REST API — это веб-API, которое построено по стандартным правилам REST.
# Django REST Framework — это инструмент, который помогает быстро создавать REST API в Django.




# Что такое сериализатор?

# Serializer — превращает Django модель в JSON и обратно.





# Основные HTTP методы

# 1. GET

# Используется для получения данных с сервера.
# Безопасный метод: ничего не изменяет в БД.
# Данные можно передавать через query params (например: ?id=5).
# Пример: открыть страницу студента. 
# GET /apartments/


# 2. POST

# Используется для создания новых данных (например, новый apartment).
# Данные передаются в теле запроса (формы или JSON).
# Не отображаются в адресной строке.
# Может изменять базу данных. 
# POST /apartments/create


# 3. PUT

# Используется для полного обновления объекта.
# Обычно в API: заменить весь объект новыми данными.
# Редко используется в HTML-формах, чаще в REST API.
# PUT /apartments/5


# 4. PATCH

# Используется для частичного обновления объекта (обновить только одно поле).
# Более гибкий, чем PUT.
# PATCH /apartments/5


# 5. DELETE

# Используется для удаления данных с сервера.
# Опасный метод: удаляет объект навсегда (если не реализовать "soft delete").
# DELETE /apartments/5


# Additional Methods ------

# 6. HEAD

# Как GET, но возвращает только заголовки, без тела.
# Используется для проверки доступности ресурса.


# 7. OPTIONS

# Запросить у сервера список доступных методов для ресурса.
# Пример: сервер может ответить, что поддерживает GET, POST, PUT, DELETE.


# GET → читать данные
# POST → создавать новые
# PUT → полностью обновить
# PATCH → частично обновить
# DELETE → удалить
# HEAD, OPTIONS → служебные



# Swagger — это инструмент, который автоматически создаёт документацию для API.

# Проще:

# вы пишете API (views, serializers)
# Swagger сам показывает все endpoints
# можно тестировать API прямо в браузере


# Когда мы используем Swagger?
# Используем, когда:

# делаем REST API (Django Rest Framework)
# хотим видеть все endpoints в одном месте
# хотим удобно тестировать API
# frontend-разработчик должен понимать API



# from django.urls import path
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="My API",
#         default_version='v1',
#         description="API documentation",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
# ]

# 'swagger/' — адрес страницы. Открыв http://127.0.0.1:8000/api/v1/swagger/,  документацию.
# schema_view.with_ui('swagger') — говорит: «показать документацию в виде интерфейса Swagger».
# cache_timeout=0 — отключает кэширование, чтобы документация всегда была свежей 
# (обновлялась сразу при изменении кода).



# Что такое Postman?
# Postman — это программа (инструмент) для тестирования API. 
# Она позволяет отправлять запросы к серверу и смотреть, 
# что он отвечает — без написания кода и без браузера.

# Представьте : вы создали REST API, но у вас ещё нет сайта или приложения, которое к нему обращается. 
# Как проверить, что API работает? Вот тут и нужен Postman — вы вручную отправляете запрос и сразу видите ответ.

# Зачем он нужен?
# Тестировать API до того, как написан фронтенд
# Проверять все методы — GET, POST, PUT, DELETE — в одном месте
# Отправлять данные (JSON, файлы) на сервер и видеть ответ
# Смотреть коды статусов (200, 404, 500) и время ответа
# Сохранять запросы в коллекции, чтобы не вводить их заново


# Основные вкладки при отправке запроса
# Params — параметры в адресе (например, фильтры ?search=django).
# Headers — заголовки запроса. Например, тут указывается формат данных или токен авторизации.
# Body — тело запроса. Самая важная вкладка для POST и PUT: здесь вы пишете данные, 
# которые отправляете на сервер. Обычно выбираете режим raw → JSON:
# json{
#     "title": "Война и мир",
#     "pages": 1225,
#     "author": 3
# }
# Authorization — здесь настраивается авторизация, если API защищён (логин, токен).

# Полезное понятие — Collections (Коллекции)
# Collection — это папка, где вы сохраняете все запросы к одному проекту. Например, коллекция «Электронная библиотека» со всеми запросами к книгам, авторам и жанрам. Это удобно: настроили один раз — пользуетесь всегда.

# Короткое резюме

# Postman — инструмент для ручного тестирования API.
# Позволяет отправлять запросы (GET, POST, PUT, DELETE) и видеть ответ сервера.
# Главные части: метод, URL, кнопка Send, вкладка Body (для отправки JSON), окно ответа.
# Помогает проверить API до того, как написан сайт или приложение.



# Serializer в DRF

# Serializer — это инструмент, который превращает данные модели в JSON и обратно.

# Он делает два ключевых действия:
# serialization → из Python объекта (модели) → JSON
# deserialization → из JSON → Python объект → модель
# То есть это переводчик данных между Django и внешним миром.


# Зачем нужны сериализаторы?

# проверяют данные (валидация)
# преобразуют типы (строки → числа)
# принимают данные в POST/PUT/PATCH
# помогают сохранять объекты в БД
# возвращают данные в API ответах


# В DRF есть 2 основных типа сериализаторов:

# Serializer (ручной, полный контроль)
# ModelSerializer (автоматический, удобный)



# 1. Serializer (ручной способ)

# Это «чистый» сериализатор.
# Ты сам указываешь поля, логики сохранения, обновления и т. д.

# Используется когда:
# нет модели
# сложный custom JSON формат
# нужна полная кастомизация

# Пример


# from rest_framework import serializers

from rest_framework import serializers
# from .models import Apartment, Block


# class ApartmentSerializer(serializers.Serializer):
#     number = serializers.IntegerField()
#     area = serializers.FloatField()
#     floor = serializers.IntegerField()
#     rooms_count = serializers.IntegerField()
#     deadline = serializers.DateField()
#     type = serializers.ChoiceField(choices=Apartment.TYPE_CHOICES)
#     block = serializers.PrimaryKeyRelatedField(queryset=Block.objects.all())

#     def create(self, validated_data):
#         return Apartment.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.number = validated_data.get('number', instance.number)
#         instance.area = validated_data.get('area', instance.area)
#         instance.floor = validated_data.get('floor', instance.floor)
#         instance.rooms_count = validated_data.get('rooms_count', instance.rooms_count)
#         instance.deadline = validated_data.get('deadline', instance.deadline)
#         instance.type = validated_data.get('type', instance.type)
#         instance.block = validated_data.get('block', instance.block)
#         instance.save()
#         return instance



# 2. ModelSerializer (автоматический)

# Это — упрощённая версия Serializer.
# Он смотрит на модель и сам генерирует:

# поля
# create()
# update()
# типы данных
# валидаторы


# class StudentModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'



# Что такое Model Manager?
# Model Manager (менеджер модели) — это объект, через который 
# Django обращается к базе данных. 
# Когда вы пишете Apartments.objects.all(), вот этот objects — и есть менеджер.
# Другими словами: менеджер — это «дверь» между вашей моделью и базой данных. 
# Через него проходят все запросы: получение, фильтрация, создание объектов.




# Токен (общее понятие)
# Токен — это строка, которая подтверждает личность/права доступа вместо того, чтобы каждый раз отправлять логин и пароль. 
# Клиент один раз логинится, получает токен, а потом отправляет его с каждым запросом (обычно в заголовке Authorization), 
# чтобы подтвердить, кто он.
# Зачем: HTTP — протокол без состояния (stateless), сервер не помнит тебя между запросами. 
# Токены решают эту проблему без серверных сессий.
# Основные виды: session-токены, JWT (JSON Web Token, содержит данные внутри себя), OAuth-токены, DRF-токены.

# DRF Token (TokenAuthentication в Django REST Framework)
# DRF встроил простую систему токенов:

# Каждый пользователь получает один фиксированный токен, который хранится в таблице БД (authtoken_token), привязанный к его user id.
# Клиент отправляет его так: Authorization: Token <токен>
# По умолчанию токен не истекает, это не JWT — просто случайная строка, по которой DRF ищет пользователя в базе.