# Telegram parsing bot
### Описание
Телеграм бот предназначен для парсинга вакансий с сайтов компаний. (В разработке, пока актуален поиск работы)

### Технологии
- Python 3.11.1
- aiogram 2.24
- bs4

### Установка
Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/Evkos-dev/parsing_vacancies.git`

`cd parsing_vacamcies`

Cоздать и активировать виртуальное окружение:

`python -m venv venv`

`source venv/Scripts/activate`

Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Создать в директории файлы:

`config.py` - в нем необходимо добавить токен своего телеграм бота token="Your token"

`vacancies_dict.json` - в нем необходимо добавить пустой словарь "{}"
