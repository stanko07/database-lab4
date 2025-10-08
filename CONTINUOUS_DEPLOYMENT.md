# 🚀 Continuous Deployment Setup Guide

## Що робить цей workflow:

Коли ви робите `git push` в гілку `main`, GitHub Actions автоматично:
1. ✅ Підключається до вашого AWS EC2 сервера
2. ✅ Завантажує останні зміни з GitHub
3. ✅ Встановлює/оновлює залежності
4. ✅ Перезапускає Flask додаток
5. ✅ Перевіряє, чи працює додаток (health check)

## 📝 Налаштування GitHub Secrets

### Крок 1: Додайте секрети в GitHub

Перейдіть: **GitHub Repository → Settings → Secrets and variables → Actions**

Створіть два секрети:

#### Secret 1: AWS_EC2_HOST
```
Name: AWS_EC2_HOST
Value: 13.62.126.107
```

#### Secret 2: AWS_PRIVATE_KEY
```
Name: AWS_PRIVATE_KEY
Value: <вміст вашого .pem файлу>
```

Щоб отримати вміст .pem файлу:
- Знайдіть ваш `.pem` файл (наприклад, `my-key.pem`)
- Відкрийте його в текстовому редакторі
- Скопіюйте весь вміст від `-----BEGIN RSA PRIVATE KEY-----` до `-----END RSA PRIVATE KEY-----`

### Крок 2: Налаштуйте Git на EC2 сервері

SSH підключіться до вашого EC2:
```bash
ssh -i your-key.pem admin@13.62.126.107
```

Виконайте команди:
```bash
cd /home/admin

# Якщо репозиторій ще не клонований:
git clone https://github.com/stanko07/database-lab4.git

# Якщо вже клонований:
cd database-lab4/lab4_for_bd
git config pull.rebase false
git remote set-url origin https://github.com/stanko07/database-lab4.git

# Налаштуйте git credential (опціонально, щоб не питати пароль):
git config --global credential.helper store
```

### Крок 3: Створіть або перевірте Virtual Environment

На EC2 сервері:
```bash
cd /home/admin/database-lab4/lab4_for_bd

# Якщо venv не існує:
python3 -m venv venv

# Активуйте та встановіть залежності:
source venv/bin/activate
pip install -r app/requirements.txt
```

## 🎯 Як це працює:

### Автоматичний deployment:
1. Змініть код локально
2. Зробіть commit: `git add . && git commit -m "Update code"`
3. Push в GitHub: `git push origin main`
4. GitHub Actions автоматично задеплоїть на EC2! ✨

### Ручний deployment:
Перейдіть: **GitHub → Actions → Deploy to AWS EC2 → Run workflow**

## 📊 Моніторинг деплоїв:

Перевіряйте статус на:
- GitHub: **Repository → Actions**
- Логи на сервері: `/home/admin/database-lab4/lab4_for_bd/flask.log`

## 🔍 Команди для перевірки на EC2:

```bash
# Перевірити чи працює Flask:
ps aux | grep "python app.py"

# Подивитись логи:
tail -f /home/admin/database-lab4/lab4_for_bd/flask.log

# Перезапустити вручну:
cd /home/admin/database-lab4/lab4_for_bd
source venv/bin/activate
pkill -f "python app.py"
nohup python app.py > flask.log 2>&1 &
```

## ✅ Тестування:

Після успішного deployment:
- 🌐 API: http://13.62.126.107:5000/candidates
- 📚 Swagger UI: http://13.62.126.107:5000/apidocs/

## 🔧 Troubleshooting:

### Якщо deployment fails:
1. Перевірте GitHub Actions logs
2. Перевірте SSH ключ в Secrets
3. Перевірте чи є git репозиторій на EC2
4. Перевірте flask.log на сервері

### Якщо Flask не запускається:
```bash
# На EC2 сервері:
cd /home/admin/database-lab4/lab4_for_bd
source venv/bin/activate
python app.py
# Подивіться на помилки
```
