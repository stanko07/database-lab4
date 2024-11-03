import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.root import register_routes
import os
import sys
from app.database import db

print(sys.path)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)  # Инициализируем сразу после создания приложения

    # Регистрируем маршруты
    register_routes(app)

    # Создаем базу данных и таблицы в контексте приложения
    with app.app_context():
        create_database()  # Создаем базу данных, если её нет
        create_tables(app)  # Создаем таблицы в базе данных
        print("Таблицы данных созданы или уже существуют.")
        populate_data()  # Заполняем таблицы, если есть SQL файл
    
    return app

def create_database():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS new_company")
    cursor.close()
    connection.close()

def create_tables(app):
    with app.app_context():  # Убедитесь, что в контексте приложения
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='123456789',
            database='new_company'
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        print(f"SQL statement: {statement}")
                        connection.rollback()
        cursor.close()
        connection.close()
        
