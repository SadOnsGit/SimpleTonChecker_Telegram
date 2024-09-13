# **SimpleTonChecker**

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

Простой чекер цены пары TON/USD, основанный на библиотеке requests. 
Стек: **python, requests**

## Возможности скрипта:
Каждые 30 секунд скрипт проверяет цену пары TON/USD и фиксирует последнее значение в переменную. 
Затем идёт сравнение с последним записанным значением, и,
если оно отличается то происходит отправка в группу телеграмма с определённым эмодзи о статусе.

Например: 

При **повышении курса** будет отправлено сообщение вида

![image](https://github.com/user-attachments/assets/19eea718-a848-48c4-9839-5db6213af6d4)

А при падении:

![image](https://github.com/user-attachments/assets/a8b793f5-2450-4250-8bb1-94beebeaa4a8)

## Локальный запуск скрипта:

**_Склонировать репозиторий к себе_**
```
git clone https://github.com/SadOnsGit/SimpleTonChecker_Telegram.git
```
**_В директории проекта создать файл .env и заполнить своими данными:_**
```
  BOT_TOKEN=''
  GROUP_CHAT_ID=''
```

  Где <b>BOT_TOKEN</b>, укажите токен бота полученный от @BotFather
  
  Где <b>GROUP_CHAT_ID</b>, укажите ID(айди) группы куда бот будет направлять сообщение. <b>ВАЖНО:</b> Бот должен состоять в группе и иметь права администратора.

**_Создать и активировать виртуальное окружение:_**

Для Linux/macOS:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Для Windows:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
**_Установить зависимости из файла requirements.txt:_**
```
pip install -r requirements.txt
```
**_Запустить бот:_**
```
python tonprice.py
```

### Автор
[Iskhakov Aidar](https://github.com/SadOnsGit)
