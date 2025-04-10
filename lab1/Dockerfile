# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY requirements.txt requirements.txt
COPY app.py app.py

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]