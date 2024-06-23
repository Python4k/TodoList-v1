# Todo List version 1

Это небольшой сайтик для создания заметок в стиле todo list

## Как собрать?

### Вариант 1

Клонировать проект
```
git clone https://github.com/Python4k/TodoList-v1.git
```

Установить зависимости
```
pip install -r requirements.txt
```

Запустить командой uvicorn
```
uvicorn app.run:app
```

или guicorn если делаете на хостинге
```
guvicorn app.run:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

##

### ~~Вариант 2~~ ( допиливаю )
Клонировать проект
```
git clone https://github.com/Python4k/TodoList-v1.git
```

Сбилдить проект через docker-compose
```
docker compose build
```

Поднять docker compose
```
docker compose up
```


## Цели ##
- [x] API для управления заметками
- [x] Frontend часть
- [ ] Добавление .env файла
- [ ] Деплой через docker

<br>


# От автора

### Привет мир!
Это мой первый самостоятельный проектик на fastapi.
В дальнейшем планирую сделать ещё несколько версий проекта, в которых будет и регистрация и групповые заметки и ещё много чего.
Если захотите поучавствовать в моём проекте - пишите!

#### [Telegram](https://t.me/python4k "https://t.me/python4k")
#### [VK](https://vk.com/python4k "https://vk.com/python4k ")
#### [LinkedIn](https://www.linkedin.com/in/python4k/ "https://www.linkedin.com/in/python4k/")
