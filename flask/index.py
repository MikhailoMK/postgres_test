from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2
from psycopg2 import Error
from datetime import datetime

DB_HOST = 'postgres'
DB_NAME = 'test'
DB_USER = 'test'
DB_PASSWORD = 'test'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_data')
def show_data():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM table1")
        people = cursor.fetchall()

        # Преобразуем даты в формат DD-MM-YYYY
        formatted_people = []
        for person in people:
            birth_date = person[3].strftime('%d-%m-%Y')  # Форматируем дату
            formatted_people.append(person[:3] + (birth_date,) + person[4:])

        cursor.close()
        connection.close()

        return render_template('show_data.html', people=formatted_people)

    except (Exception, Error) as error:
        return jsonify({'error': str(error)}), 500

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        birth_date = request.form['birth_date']
        phone_number = request.form['phone_number']

        try:
            connection = psycopg2.connect(
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                database=DB_NAME
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO table1 (f_name, l_name, birth_date, phone_number) VALUES (%s, %s, %s, %s)",
                (f_name, l_name, birth_date, phone_number)
            )
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('index'))

        except (Exception, Error) as error:
            return jsonify({'error': str(error)}), 500
    return render_template('add_data.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
