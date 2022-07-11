# Получение данных о погоде от OpenWeather API
### Описание. 
Программа, которая получает текущие географические координаты пользователя и показывает данные о погоде для его местоположения от OpenWeather API. Автор: Бурцев Никита. Технологии: Python.

### Как запустить проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <cсылка_на_проект_в_git>
cd weather
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
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
В директории проекта создать файл .env и добавить в него строчку:

```
Запустить файл main.py
