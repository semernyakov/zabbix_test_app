# Asynchronous analyzer for Zabbix Monitoring Systems (based on AIOHTTP)

Асинхронный анализатор (парсер) дублирующихся хостов для систем мониторинга на базе ZABBIX (https://www.zabbix.com/)

 ## Базовая архитектура

 * Python 3.7 - Без комментариев, https://www.python.org/downloads/
 * Portainer - Управляйте Docker средами с через веб-интерфейс https://www.portainer.io/installation
 * Pipenv - Управление виртуальными окружением Python https://pipenv.pypa.io/en/latest/
 * Docker - Контейнерная виртуализация https://docs.docker.com/install/
 * Zabbix - Система мониторинга https://www.zabbix.com/documentation/current/ru/manual/installation 
 
NB: приложение тестировалось на Zabbix API Version 4.4.6

## Установка Python зависимостей

Создайте виртуальное окружение и установите зависимости

```bash
pipenv install
```
## Установка и запуск контейнера с образом Portainer 

 ```bash
docker volume create portainer_data
docker run -d -p 8655:8655 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

Открываем в браузере http://127.0.0.1:9000/ (http://locahost:9000/) и создаём нового пользователяб полсе авторизации вы можете полноценно 
управлять вашими Docker resources (containers, images, volumes, networks ...)

## Установка и запуск образа Zabbix appliance 4.4
В данном примере мы установим один образ (Image: 'zabbix/zabbix-appliance:ubuntu-latest') и запустим сразу два контейнера 
(Container(s): 'zabbix-server-1', 'zabbix-server-2')
```bash
docker run --name zabbix-server-1 -p 80:80 -p 10051:10051 -d zabbix/zabbix-appliance:ubuntu-latest
docker run --name zabbix-server-2 -p 80:80 -p 10052:10052 -d zabbix/zabbix-appliance:ubuntu-latest
```
## Авторизация в веб-интерфейсе
Логин-Пароль: Admin:zabbix

## Коммандная строка

Консоль docker
```bash
docker exec -ti zabbix-server-1 /bin/bash
docker exec -ti zabbix-server-2 /bin/bash
```

## Автоматическое создание фай ковых данных
```bash
python ./zabbix_test/inithosts.py
```

## Настройки
см ./zabbix_test/config.py

## Разварачиваем фронт

Опционально! Обновляем node, если нужно!
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
node -v 
```
Запускаем фронт
```bash
cd ./zabbix_test/vueapp
yarn install
yarn serve
```
Подробности: vueapp/README.md