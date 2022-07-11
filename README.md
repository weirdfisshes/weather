# Получение данных о погоде от OpenWeather API
### Описание. 
Программа, которая получает текущие географические координаты пользователя и показывает данные о погоде для его местоположения от OpenWeather API. Автор: Бурцев Никита. Технологии: Python 3, geocoder, dotenv, Git.

### Как запустить проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <cсылка_на_проект_в_git>
cd weather
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Зарегистрироваться на https://openweathermap.org/ и получить токен.
В директории проекта создать файл .env и добавить в него переменную TOKEN, равную вашему токену:

```
TOKEN = "your_token"
```
Запустить файл main.py
