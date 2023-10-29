FROM python:3.11.5-alpine3.18    # Образ, на основе которого создаём наш контейнер

WORKDIR /app   # Рабочая директория внутри контейнера

COPY . /app   # Копируем всё из рабочей среды (где находится Dockerfile) в рабочую директорию контейнера

RUN pip install --no-cache-dir -r /app/requirements.txt   # Устанавливаем все зависимости из файла requirements.txt
в рабочую директорию; флаг --no-cache-dir говорит не кэшировать зависимостей

ENV PYTHONDONTWRITEBYTECODE 1  # Указывает Python не создавать кэш файлы с байт кодом рус
ENV PYTHONUNBUFFERED 1  # Указывает Python что нет необходимости кэшировать ввод/вывод

EXPOSE 8000  # Нужно открыть на 8000 порту данный контейнер
