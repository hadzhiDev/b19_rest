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






# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response({'error': 'Not found'}, status=404)

#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=204)






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

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
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





# Основные HTTP методы

# 1. GET

# Используется для получения данных с сервера.
# Безопасный метод: ничего не изменяет в БД.
# Данные можно передавать через query params (например: ?id=5).
# Пример: открыть страницу movies. 
# GET /movies/


# 2. POST

# Используется для создания новых данных (например, новый film).
# Данные передаются в теле запроса (формы или JSON).
# Не отображаются в адресной строке.
# Может изменять базу данных. 
# POST api/v1/movies/


# 3. PUT

# Используется для полного обновления объекта.
# Обычно в API: заменить весь объект новыми данными.
# Редко используется в HTML-формах, чаще в REST API.
# PUT /api/v1/movies/5/



# 4. PATCH

# Используется для частичного обновления объекта (обновить только одно поле).
# Более гибкий, чем PUT.
# PATCH /api/v1/movies/5/


# 5. DELETE

# Используется для удаления данных с сервера.
# Опасный метод: удаляет объект навсегда (если не реализовать "soft delete").
# DELETE /students/5


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