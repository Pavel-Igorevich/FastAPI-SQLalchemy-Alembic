#!/bin/bash


# Функция для запуска приложения
start() {
    # Активируем виртуальное окружение
    source "venv/bin/activate"
    # Запускаем приложение FastAPI с Uvicorn
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload &
    echo "FastAPI приложение запущено."
}

# Функция для остановки приложения
stop() {
    # Найти процесс Uvicorn и убить его
    pkill -f "uvicorn main:app"
    echo "FastAPI приложение остановлено."
}

# Функция для проверки статуса приложения
status() {
    if pgrep -f "uvicorn main:app" > /dev/null
    then
        echo "FastAPI приложение запущено."
    else
        echo "FastAPI приложение не запущено."
    fi
}

# Обработка аргументов
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
        status
        ;;
    *)
        echo "Используйте 'start', 'stop' или 'status'."
        exit 1
        ;;
esac
