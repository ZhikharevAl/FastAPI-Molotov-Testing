# Установите конкретную версию Ubuntu
FROM ubuntu:latest
LABEL authors="1"

# Установите рабочую директорию в /app
WORKDIR /app

# Скопируйте текущую директорию в рабочую директорию /app
COPY . /app

# Обновите список пакетов
RUN apt-get update

# Установите python и pip
RUN apt-get install -y python3.10 python3-pip

# Установите зависимости Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Очистите кэш apt
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Откройте порт 8000 для обслуживания вашего приложения
EXPOSE 8000

# Запустите приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
