FROM python:3.8-alpine

ARG run_env
ENV env $run_env

LABEL "creator"="MaksimTsybikov"

# Указываем директорию в которой будем работать внутри докера
WORKDIR ./usr/mytasks

# Обновляем базовый образ
RUN apk update && apk upgrade && apk add bash

# Копируем отдельно файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости внутри контейнера
RUN pip3 install -r requirements.txt

# Копируем файлы внутрь контейнера
COPY . .

# Запускаем тесты
CMD pytest -m "$env" -s -v tests/*