# Проект на Flask с PostgreSQL

Этот проект представляет собой веб-приложение на базе Flask и PostgreSQL, развернутое с помощью Docker. Приложение включает два iamge: один для Flask и один для БД PostgreSQL.

## Структура проекта

Проект состоит из следующих компонентов:
1. **Flask (веб-приложение)** — предоставляет три страницы:
   - Главная страница
   - Страница для просмотра данных
   - Страница для добавления новых данных в базу

2. **PostgreSQL (база данных)** — используется для хранения данных, таблица уже заполнена данными.

## Инструкции по запуску

1. **Клонируйте репозиторий:**

   ```
   git clone https://github.com/MikhailoMK/postgres_test.git
   cd postgres_test
   ```
2. **Запуск docker-compose:**
   ```
   docker-compose up --build
   ```
3. **Перейдите по адресу <ваш_ip>:5000**
