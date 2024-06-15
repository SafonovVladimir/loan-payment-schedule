# Loan Schedule API

## Опис завдання
Цей API сервіс призначений для побудови та зміни графіка платежів за кредитом.

## Технології, які використані в проекті
- Docker
- Django
- Django REST Framework
- SQLite

## Інструкція по розгортанню

1. Клонувати репозиторій
    ```sh
    git clone <repo_url>
    cd <repo_directory>
    ```

2. Запустити Docker
    ```sh
    docker-compose up --build
    ```

3. API буде доступне за адресою `http://localhost:8000/`

## Використання

### Створення графіка платежів
- Метод: POST
- URL: `/api/loans/`
- Приклад запиту:
    ```json
    {
        "amount": 1000,
        "loan_start_date": "10-01-2024",
        "number_of_payments": 4,
        "periodicity": "1m",
        "interest_rate": 0.1
    }
    ```

### Зміна суми тіла платежу
- Метод: PATCH
- URL: `/api/schedules/<payment_id>/`
- Приклад запиту:
    ```json
    {
        "principal": 50
    }
    ```

## Тести

Запустити тести:
```sh
docker-compose run web python manage.py test
