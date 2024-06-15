# Loan Schedule API

## Цей API сервіс призначений для створення запитів для побудови та зміни графіків платежів за кредитами.

## Технології, які використані в проекті
- Django
- Django REST Framework
- SQLite
- Docker 

## Інструкція по розгортанню

### Клонування репозиторію
1. Клонувати репозиторій
    ```sh
    git clone https://github.com/SafonovVladimir/loan-payment-schedule
    cd loan-payment-schedule
    ```

### Налаштування середовища
2. Створити віртуальне середовище та активувати його
    ```sh
    python -m venv venv
    source venv/bin/activate  # На Windows використовуйте venv\Scripts\activate
    ```

3. Встановити залежності
    ```sh
    pip install -r requirements.txt
    ```

### Міграції бази даних
4. Застосувати міграції бази даних
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

### Запуск проекту
5. Запустити сервер розробки
    ```sh
    python manage.py runserver
    ```

### Використання Docker
6. Якщо ви віддаєте перевагу використанню Docker, можна скористатися Docker Compose для запуску проекту:
    ```sh
    docker-compose up --build
    ```

API буде доступне за адресою `http://localhost:8000/`.

## Використання

### Створення графіка платежів
- Метод: POST
- URL: `/api/loans/`
- Приклад запиту:
    ```json
    {
        "amount": 10000,
        "loan_start_date": "01-01-2025",
        "number_of_payments": 5,
        "periodicity": "3m",
        "interest_rate": 0.15
    }
    ```

### Зміна суми тіла платежу
- Метод: PATCH
- URL: `/api/payments/<payment_id>/modify-principal/`
- Приклад запиту:
    ```json
    {
        "new_principal": 1000
    }
    ```

## Тести

1. Запустити тести
    ```sh
    docker-compose run web python manage.py test
    ```