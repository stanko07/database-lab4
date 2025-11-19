import os

class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    USE_MYSQL = os.getenv("USE_MYSQL", "false").lower() == "true"

    # ---------- PRODUCTION (AWS ECS + RDS) ----------
    if FLASK_ENV == "production":
        SQLALCHEMY_DATABASE_URI = (
            "mysql+pymysql://admin:vfhnf111@vacancies-company.cp0suqqgsip3.eu-north-1.rds.amazonaws.com:3306/vacancies_company"
        )

    # ---------- FORCE MySQL Locally for Debug ----------
    elif USE_MYSQL:
        SQLALCHEMY_DATABASE_URI = (
            "mysql+pymysql://admin:vfhnf111@vacancies-company.cp0suqqgsip3.eu-north-1.rds.amazonaws.com:3306/vacancies_company"
        )

    # ---------- LOCAL SQLITE (default) ----------
    else:
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, '..', 'instance', 'app.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
