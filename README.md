#Тестовое задание: Система управления задачами

## Установка

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

## Запуск приложения

Для запуска приложения выполните следующую команду:

```cmd

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

- **Конечная точка:** `/`
- **Метод:** `GET`
- **Описание:** получение информации о пользователе.
- **Тело запроса:**
  - `user` (RegUser): Данные пользователя, необходимые для регистрации.
- **Ответ:** Возвращает авторизированного пользователя.

### 3. Получение задачи

- **Конечная точка:** `/task_{id}`
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

- **Конечная точка:** `/all}`
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

- **Конечная точка:** `/create}`
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

- **Конечная точка:** `/update/{task_id}`
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

- **Конечная точка:** `/delete/{task_id}`
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
##тестирование энд ту энд
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
