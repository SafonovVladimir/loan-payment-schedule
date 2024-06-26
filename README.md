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
   
4. Налаштування змінних середовища:
    - Створіть файл `.env` у директорії, в якій знаходиться файл `manage.py`.
    - Додайте до нього ваш секретний ключ та інші необхідні змінні середовища:
        ```
        SECRET_KEY=your_secret_key
        DEBUG=True  # або False в залежності від середовища
        ```

### Міграції бази даних
5. Застосувати міграції бази даних
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

### Запуск проекту
6. Запустити сервер розробки
    ```sh
    python manage.py runserver
    ```

### Використання Docker
7. Якщо ви віддаєте перевагу використанню Docker, можна скористатися Docker Compose для запуску проекту:
    ```sh
    docker-compose up --build
    ```
API буде доступне за адресою `http://0.0.0.0:8081/`.

## Використання

### Головний екран API

![screenshot](/loan_payment_schedule/readme_images/main_screen.png "Main_screen")

### Додавання клієнтів

- Метод: POST
- URL: `/clients/`
- Приклад запиту:
    ```json
    {
        "name": "Myhailo Grushevsky"
    }
    ```

### Створення графіка платежів
- Метод: POST
- URL: `/loans/`
- Приклад запиту:
    ```json
    {
        "client": "Myhailo Grushevsky"
        "amount": 10000,
        "loan_start_date": "01-01-2025",
        "number_of_payments": 5,
        "periodicity": "3m",
        "interest_rate": 0.15
    }
    ```
  
### Перегляд списку платежів
- Метод: GET
- URL: `/schedules/`

![screenshot](/loan_payment_schedule/readme_images/schedule_screen.png)

### Зміна суми тіла платежу
- Метод: PATCH
- URL: `/payments/<payment_id>/modify-principal/`
- Приклад запиту:
    ```json
    {
        "new_principal": 10
    }
    ```
![screenshot](/loan_payment_schedule/readme_images/modify-principal.png)

Цей README.md файл містить інформацію про налаштування змінних середовища, 
використання `load_dotenv()` для завантаження секретних ключів та інструкції по встановленню, 
використанню та тестуванню проекту.
