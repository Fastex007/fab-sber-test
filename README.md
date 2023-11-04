# fab-sber-test
[![srv](https://github.com/Fastex007/fab-sber-test/actions/workflows/main.yml/badge.svg)](https://github.com/Fastex007/fab-sber-test/actions/workflows/main.yml)

### Сервис развернут на http://158.160.120.94/

## Описание проекта
Тестовый проект на Flask-AppBuilder.
Можно авториоваться через GitHub.
Реализована кастомная реализация с использованием логина и пароля.

## Доступные эндпоинты
* ```/``` - индексная страница.
* ```/login/``` - авторизация через GitHub.
* ```/auth/``` - авторизация через кастомную логинилку с использвованием логина и пароля.
* ```/auth/logout/``` - выход.

## Используемые зависимости
```
Authlib==1.2.1  # пакет для выполнения авторизации через OAUTH провайдеров.
Flask-AppBuilder==4.3.9  # фреймворк на основе которого сделан проект.
python-dotenv==1.0.0  # для чтения переменных окружения из файла.
requests==2.31.0  # пакет для выполнения запрсоов.
```

## Запуск проекта
* #### Клонировать репозиторий
```
git clone https://github.com/Fastex007/multithread_web_server.git
```

* #### Выполнить команду
```
docker-compose up -d
```

## Переменные окружения
* ```GH_CLIENT_ID``` - IP адрес сервиса
* ```GH_CLIENT_SECRET``` - IP адрес сервиса
* ```SECRET_KEY``` - IP адрес сервиса

## Автор
#### Pronkin Oleg
```
https://github.com/Fastex007
```
