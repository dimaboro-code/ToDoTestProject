
# 📝 ToDo List API

Минимальный backend-сервис для управления списком задач (ToDo) с REST API, авторизацией и парсингом данных с сайта Astana Hub. Развертывание через Docker Compose.

## 🚀 Стек технологий

- Python 3.12+
- Django 5+
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- JWT
- Swagger (drf-yasg)
- Requests, BeautifulSoup (для парсинга)

---

## ⚙️ Быстрый старт

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

### 2. Соберите и запустите контейнеры
```bash
docker compose up --build
```

Сервер будет доступен по адресу: `http://localhost:8000` 
> При запуске проект создает суперюзера с данными из .env файла
---

## 📚 Документация

### Swagger UI
Доступна по адресу:  
```
http://localhost:8000/docs/
```

---

## 🔐 Аутентификация

### Регистрация
`POST /auth/register/`  
**Поля:** `email`, `username`, `password`

### Логин
`POST /auth/login/`  
**Поля:** `email`, `password`  
**Ответ:** JWT-токен

> Все эндпоинты `/tasks/` требуют авторизации.
> Авторизация возможно как по юзернейму, так и по емейлу

---

## 📌 Эндпоинты задач

| Метод | URL | Описание |
|-------|-----|----------|
| `POST` | `/tasks/` | Создание новой задачи |
| `GET` | `/tasks/` | Список задач (фильтрация по `completed`, `title`) |
| `GET` | `/tasks/{id}/` | Получение одной задачи |
| `PUT/PATCH` | `/tasks/{id}/` | Обновление задачи |
| `DELETE` | `/tasks/{id}/` | Удаление задачи |

### Фильтрация
Пример:
```
/tasks/?completed=true&title=meeting
```

---

## 🌐 Парсинг участников Astana Hub

`GET /parser/parse/`  
Собирает первых 10 участников [технопарка Astana Hub](https://astanahub.com/ru/service/techpark/) и сохраняет их в базу данных.

`GET /parser/`  
Показывает список собранных участников Astana Hub.

---

## 🧪 Тесты

Запуск тестов внутри контейнера:
```bash
docker compose exec web pytest
```

---

## 🛠 Дополнительно

- ✅ Пагинация списка задач
- ✅ Автообновление поля `updated_at`
- ✅ Минимальная админка для управления задачами
- ✅ Black + PEP8 форматирование

---

## 📂 Структура проекта

```
todo_api/
├── todo_api/          # Основное приложение
├── users/             # Авторизация и регистрация
├── parser/            # Парсинг Astana Hub
├── tasks/             # ToDo лист
├── manage.py
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📄 Лицензия

MIT License

