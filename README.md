# Тестовое задание: Система управления задачами

## Установка
Для запуска проекта требуется docker-compose!

1. Клонируйте репозиторий:

    ```cmd
    git clone https://github.com/Deniska1644/eremech_rus.git
    ```

2. Перейдите в директорию проекта:

    ```cmd
    cd какой-то\путь\eremech_rus
    ```

3. Запуск приложения:
    ```cmd
    docker-compose build
    docker-compose up -d
    ```

## эндпойнты

### 1. Регистрация пользователя

- **Конечная точка:** `/registrate`
- **Метод:** `POST`
- **Описание:** Регистрирует нового пользователя.
- **Тело запроса:**
  - `user` (RegUser): Данные пользователя, необходимые для регистрации.
- **Ответ:** Возвращает результат процесса создания пользователя.

#### Пример запроса
```json
POST /user/registrate
{
  "username": "example_user",
  "password": "secure_password"
}
```

### 2. Получение информации о пользователе

- **Конечная точка:** `user/`
- **Метод:** `GET`
- **Описание:** получение информации о пользователе.
- **Тело запроса:**
  - `user` (RegUser): Данные пользователя, необходимые для регистрации.
- **Ответ:** Возвращает авторизированного пользователя.

### 3. Получение задачи

- **Конечная точка:** `task/{id}/get`
- **Метод:** `GET`
- **Описание:** получение задачи авторизованного пользователя.

#### Пример ответа
```json
GET /user/registrate
{
  "id": 74,
  "title": "string",
  "description": "string",
  "due_data": "2025-02-05"
}
```

### 4. Получение задач

- **Конечная точка:** `task/all}`
- **Метод:** `GET`
- **Описание:** получение всех задач авторизованного пользователя.

#### Пример ответа
```json
GET /user/registrate
[
  {
    "id": 67,
    "title": "string",
    "description": "string",
    "due_data": "2025-02-05"
  },
  {
    "id": 68,
    "title": "string",
    "description": "string",
    "due_data": "2025-02-05"
  }
]
```

### 5. Создание задачи

- **Конечная точка:** `task/create}`
- **Метод:** `POST`
- **Описание:** создание задачи для авторизованного пользователя.
#### Пример запроса
```json
{
  "title": "string",
  "description": "string",
  "due_data": "2025-02-05"
}
```

#### Пример ответа
```json
{
  "status": "successful",
  "id": 75
}
```

### 6. Обновление задачи

- **Конечная точка:** `task/{task_id}/update`
- **Метод:** `PATCH`
- **Описание:** обновление задачи для авторизованного пользователя.
#### Пример запроса
```path
  task_id = *
```
```json
{
  "title": "string",
  "description": "string",
  "due_data": "2025-02-05"
}
```

#### Пример ответа
```json
{
  "status": "successful",
  "id": 66
}
```

### 7. Удаление задачи

- **Конечная точка:** `task/{task_id}/delete`
- **Метод:** `DELETE`
- **Описание:** удаление задачи для авторизованного пользователя.
#### Пример запроса
```path
  task_id = *
```


#### Пример ответа
```json
{
  "status": "successful",
  "id": 66,
  "operation": "delete"
}
```
## тестирование end-to-end
Для запуска тестирование требуется установка зависимостей + запущенное приложение и бд.

1. Перейдите в директорию проекта:

    ```cmd
    cd какой-то\путь\eremech_rus
    ```
2. Запустите установку зависимостей
    ```cmd
    pip install -r requirements.txt
    ```
3. Перейдите в дирректорию с тестами
    ```cmd
    cd tests
    ```
4. Запуск тестов
   ```cmd
   pytest -v
   ```
