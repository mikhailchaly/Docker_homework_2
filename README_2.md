# Команды для запуска контейнера с backend-сервером

## Сборка Docker-образа с заданием ему имени

docker build . --tag=stocks_products:1.0

## Просмотр доступных локальных образов

docker images

## Запуск Docker-контейнера с заданием ему имени и с пробросом порта

docker run -d --name stocks -p 8000:8000 stocks_products:1.0

## Просмотр работающих контейнеров

docker ps

## Просмотр всех существующих на хосте контейнеров

docker ps --all
