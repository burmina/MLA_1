#!/bin/bash

# Установка системных зависимостей
sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

# Создание и активация виртуального окружения
python3 -m venv ml_venv
source ml_venv/bin/activate

# Установка пакетов через pip с явным разрешением
pip install --break-system-packages numpy pandas scikit-learn

# Выполнение скриптов
echo "=== Запуск data_creation.py ==="
python3 data_creation.py

echo "=== Запуск model_preprocessing.py ==="
python3 model_preprocessing.py

echo "=== Запуск model_preparation.py ==="
python3 model_preparation.py

echo "=== Запуск model_testing.py ==="
python3 model_testing.py > test_results.txt

# Сохранение результатов
echo "=== Результаты тестирования ==="
cat test_results.txt
echo "MSE: $(grep -oE '[0-9.]+' test_results.txt | tail -1)" > metrics.txt
