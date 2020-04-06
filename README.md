## Приложения по созданию заказов

####

```shell script
# запуск локально
poetry run python manage.py runserver

# создание миграций
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

### Управление пакетами
```shell script
poetry install --develop # установка локально
poetry install # установка на сервере

# добавление пакетов нужных для приложения
poetry add django  

# добавление пакетов нужных для разработки
poetry add --dev isort  
```

### Перед созданием коммитов
```shell script
poetry run unify --in-place . -r
poetry run isort
poetry run flake8
```
