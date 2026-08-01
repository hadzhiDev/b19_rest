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



# Generic views — это готовые классы, которые уже содержат типовую логику CRUD.
# Ты просто указываешь:
#  • какой queryset
#  • какой сериализатор
#  • какие пермишены

# И всё — DRF сам делает остальное.

# Generic views = меньше кода, меньше ошибок, быстрее разработка.

# Пример с ListCreateAPIView:


# class StudentListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer




# Что такое ViewSet в DRF

# ViewSet — это класс, который объединяет сразу несколько действий 
# (list, retrieve, create, update, delete) в одном месте.



# Что такое Router

# Router — это автоматический генератор URL-ов для ViewSet-ов.




# Inlines
# Paginations in ViewSets
# Filters in ViewSets
# Permissions in ViewSets







# DRF: Пагинация и Фильтрация

## 1. Зачем это нужно

# Отсюда два инструмента:

# - **Пагинация** — отвечаем не всем набором, а «страницей» (куском).
# - **Фильтрация** — отдаём только те объекты, которые подходят под условия из query-параметров.

# Порядок работы в DRF всегда такой:

# ```
# get_queryset() → filter_queryset() → paginate_queryset() → serializer
# ```

# Сначала фильтруем, потом режем на страницы. Это важно: пагинация применяется уже к отфильтрованному набору.

# ---

# ## 2. Пагинация

# Пагинация работает **только в `ListAPIView` / `ListModelMixin`** (то есть в `list`-экшене). Для `retrieve`, `create` и т.д. она не применяется.

# ### Глобальная настройка

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 20,
# }


# Важный нюанс: если указать только `DEFAULT_PAGINATION_CLASS` без `PAGE_SIZE`, пагинация **не заработает**.

#  2.1 PageNumberPagination


# from rest_framework.pagination import PageNumberPagination

# class ProductPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'  # клиент может менять размер: ?page_size=50
#     max_page_size = 100                  # но не больше 100
#     page_query_param = 'page'


# Запрос: `/api/products/?page=3&page_size=50`

# Ответ:

# json
# {
#   "count": 500,
#   "next": "http://api.../products/?page=4",
#   "previous": "http://api.../products/?page=2",
#   "results": [ ... ]
# }
# 

# Под капотом: `LIMIT 50 OFFSET 100`.




# ### 2.2 LimitOffsetPagination

# Клиент сам управляет окном.

# class ProductPagination(LimitOffsetPagination):
#     default_limit = 20
#     max_limit = 100

# Запрос: `/api/products/?limit=20&offset=40`

# Формат ответа тот же (`count / next / previous / results`).


# ### 2.3 CursorPagination

# Самая «правильная» для больших и живых данных. Вместо номера страницы клиент получает непрозрачный курсор — закодированную позицию в наборе.

# ```python
# class ProductPagination(CursorPagination):
#     page_size = 20
#     ordering = '-created_at'  # обязательно! поле должно быть уникальным/неизменяемым
# ```

# Запрос: `/api/products/?cursor=cD0yMDI2LTA4LTAx`

# Ответ: только `next`, `previous`, `results` — **без `count`**.

# - ➕ Стабильная производительность независимо от глубины (использует `WHERE created_at < ...`, а не `OFFSET`). Нет «проблемы сдвига»: если во время просмотра добавили новые записи, при offset-пагинации ты увидишь один и тот же объект дважды или пропустишь его — с курсором такого нет.
# - ➖ Нельзя прыгнуть на страницу №7, нет общего количества.

# **Практическое правило:** ленты, чаты, логи, бесконечный скролл → Cursor. Админки и каталоги с номерами страниц → PageNumber.

# ### Применение к конкретной вьюхе

# ```python
# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = ProductPagination  # или None, чтобы отключить
# ```

# ### Кастомный формат ответа

# ```python
# class CustomPagination(PageNumberPagination):
#     page_size = 20

#     def get_paginated_response(self, data):
#         return Response({
#             'total': self.page.paginator.count,
#             'page': self.page.number,
#             'pages': self.page.paginator.num_pages,
#             'results': data,
#         })
# ```

# ---

# ## 3. Фильтрация

# Фильтр в DRF — это класс с методом `filter_queryset(self, request, queryset, view)`, который возвращает новый queryset. Их можно комбинировать: они применяются цепочкой, по очереди.

# ```python
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend',
#         'rest_framework.filters.SearchFilter',
#         'rest_framework.filters.OrderingFilter',
#     ]
# }
# ```

# ### 3.1 Самый простой способ — переопределить `get_queryset()`

# ```python
# class ProductListView(ListAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         qs = Product.objects.all()
#         category = self.request.query_params.get('category')
#         if category:
#             qs = qs.filter(category__slug=category)
#         return qs
# ```

# Работает, но при 5–10 параметрах превращается в лапшу из `if`. Отсюда — бэкенды фильтрации.

# ### 3.2 SearchFilter — текстовый поиск

# ```python
# from rest_framework.filters import SearchFilter

# class ProductListView(ListAPIView):
#     filter_backends = [SearchFilter]
#     search_fields = ['name', 'description', 'category__name']
# ```

# Запрос: `?search=ноутбук` → ищет по всем перечисленным полям через `OR` с `icontains`.

# Префиксы в `search_fields` меняют поведение:

# | Префикс | Значение |
# |---|---|
# | `'name'` | `icontains` (по умолчанию) |
# | `'^name'` | `istartswith` — начинается с |
# | `'=name'` | `iexact` — точное совпадение |
# | `'@name'` | полнотекстовый поиск (только PostgreSQL) |
# | `'$name'` | regex |

# ### 3.3 OrderingFilter — сортировка

# ```python
# from rest_framework.filters import OrderingFilter

# class ProductListView(ListAPIView):
#     filter_backends = [OrderingFilter]
#     ordering_fields = ['price', 'created_at', 'name']  # что разрешено
#     ordering = ['-created_at']                          # по умолчанию
# ```

# Запрос: `?ordering=-price` (минус = по убыванию), можно несколько: `?ordering=category,-price`.

# Важно: указывай `ordering_fields` явно. Если поставить `'__all__'`, клиент сможет сортировать по любому полю, включая тяжёлые для БД.

# ### 3.4 django-filter — основной инструмент

# Устанавливаем: `pip install django-filter`, добавляем `'django_filters'` в `INSTALLED_APPS`.

# Простой вариант — просто перечислить поля:

# ```python
# from django_filters.rest_framework import DjangoFilterBackend

# class ProductListView(ListAPIView):
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['category', 'in_stock', 'brand']
# ```

# Запрос: `?category=3&in_stock=true`

# Продвинутый вариант — свой `FilterSet` с диапазонами и кастомной логикой:

# ```python
# import django_filters

# class ProductFilter(django_filters.FilterSet):
#     min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
#     max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
#     created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
#     name = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Product
#         fields = ['category', 'brand', 'in_stock']


# class ProductListView(ListAPIView):
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = ProductFilter
# ```

# Запрос: `?min_price=1000&max_price=5000&category=3&created_after=2026-01-01`

# Дополнительно бывает `ModelMultipleChoiceFilter` (несколько значений: `?tags=1&tags=2`), `BooleanFilter`, и метод-фильтры:

# ```python
#     is_discounted = django_filters.BooleanFilter(method='filter_discounted')

#     def filter_discounted(self, queryset, name, value):
#         return queryset.filter(old_price__isnull=not value)
# ```

# ---

# ## 4. Всё вместе

# ```python
# class ProductListView(ListAPIView):
#     queryset = Product.objects.select_related('category').all()
#     serializer_class = ProductSerializer
#     pagination_class = ProductPagination
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_class = ProductFilter
#     search_fields = ['name', 'description']
#     ordering_fields = ['price', 'created_at']
#     ordering = ['-created_at']
# ```

# Запрос:

# ```
# /api/products/?search=ноутбук&min_price=1000&ordering=-price&page=2&page_size=20
# ```

# Порядок выполнения: базовый queryset → django-filter → поиск → сортировка → пагинация → сериализация.

# ---

# ## 5. На что обратить внимание (частые ошибки)

# 1. **Нет сортировки — нестабильная пагинация.** Если queryset не отсортирован, БД может вернуть строки в разном порядке, и на второй странице появятся дубли. Всегда задавай `ordering` или `Meta.ordering` в модели.
# 2. **N+1 запросов.** Пагинация не спасает от N+1: 20 объектов × запрос на каждую связь = 21 запрос. Используй `select_related` / `prefetch_related`.
# 3. **`COUNT(*)` на больших таблицах** — реальная причина медленных ответов. Если таблица огромная, переходи на `CursorPagination`.
# 4. **Не ограничил `max_page_size`** — клиент запросит `?page_size=1000000` и положит сервер.
# 5. **Фильтровать нужно в БД, а не в Python.** `[p for p in Product.objects.all() if p.price > 100]` вытянет всю таблицу в память.
# 6. **Пагинация не работает в `retrieve`/`create`** — только в списковых экшенах.

# ---

# ## 6. Вопросы для проверки понимания

# 1. Почему `CursorPagination` не возвращает `count`?
# 2. Что произойдёт, если во время листания страниц кто-то добавит новую запись в начало списка — при `PageNumberPagination` и при `CursorPagination`?
# 3. Что раньше выполняется — фильтрация или пагинация, и почему это важно?
# 4. Чем `SearchFilter` отличается от `django-filter`? Когда что выбирать?
# 5. Зачем нужен `max_page_size`?
