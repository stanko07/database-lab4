import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from app.config import Config
from app.root import register_routes
import os
import sys
from app.database import db
from sqlalchemy import text

print(sys.path)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Swagger configuration
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    
    swagger_template = {
        "info": {
            "title": "Vacancies Company API",
            "description": "API for managing vacancies, candidates, companies and other HR data",
            "version": "1.0.0"
        }
    }
    
    Swagger(app, config=swagger_config, template=swagger_template)
    db.init_app(app)

    register_routes(app)

    with app.app_context():
        create_tables(app)
        # Populate data depending on which DB is used
        if _is_mysql(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database()  # optional connectivity check for RDS
            populate_data_mysql()
        else:
            populate_data_sqlalchemy()
    return app


def _is_mysql(uri: str) -> bool:
    return uri.startswith("mysql")


def create_database():
    # Only attempt RDS connectivity check if using MySQL
    try:
        import mysql.connector  # import lazily to avoid dependency when using SQLite
        connection = mysql.connector.connect(
            host='vacancies-company.cp0suqqgsip3.eu-north-1.rds.amazonaws.com',
            user='admin',
            password='vfhnf111',
            database='new_company',
            port=3306
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("Соединение с AWS RDS успешно!")
        cursor.close()
        connection.close()
    except Exception as error:
        print(f"Ошибка соединения с AWS RDS: {error}")


def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data_mysql():
    # Execute SQL file directly against RDS (optional)
    sql_file_path = os.path.abspath('data.sql')
    if not os.path.exists(sql_file_path):
        print(f"SQL файл не найден: {sql_file_path}")
        return
    try:
        import mysql.connector  # import lazily
        connection = mysql.connector.connect(
            host='vacancies-company.cp0suqqgsip3.eu-north-1.rds.amazonaws.com',
            user='admin',
            password='vfhnf111',
            database='new_company',
            port=3306
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
            sql_text = sql_file.read()
            for statement in [s.strip() for s in sql_text.split(';') if s.strip()]:
                try:
                    cursor.execute(statement)
                    connection.commit()
                except mysql.connector.Error as error:
                    print(f"Error executing SQL statement: {error}")
                    print(f"SQL statement: {statement}")
                    connection.rollback()
        cursor.close()
        connection.close()
        print("Данные успешно загружены (MySQL)!")
    except Exception as error:
        print(f"Ошибка при загрузке данных (MySQL): {error}")


def populate_data_sqlalchemy():
    # Use the active SQLAlchemy engine (works for SQLite)
    sql_file_path = os.path.abspath('data.sql')
    if not os.path.exists(sql_file_path):
        print(f"SQL файл не найден: {sql_file_path}")
        return
    try:
        with open(sql_file_path, 'r', encoding='utf-8') as f:
            sql_text = f.read()
        # Split on ';' and execute non-empty statements
        statements = [s.strip() for s in sql_text.split(';') if s.strip()]
        with db.engine.begin() as conn:
            for stmt in statements:
                conn.exec_driver_sql(stmt)
        print("Данные успешно загружены (SQLAlchemy/SQLite)!")
    except Exception as error:
        print(f"Ошибка при загрузке данных (SQLAlchemy): {error}")

