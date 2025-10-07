import os

class Config:
    # Use SQLite for local testing, MySQL for production
    # To use MySQL, set environment variable: USE_MYSQL=true
    if os.getenv('USE_MYSQL', 'false').lower() == 'true':
        SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:vfhnf111@vacancies-company.cp0suqqgsip3.eu-north-1.rds.amazonaws.com:3306/vacancies_company"
    else:
        # SQLite for local development
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, '..', 'instance', 'app.db')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

