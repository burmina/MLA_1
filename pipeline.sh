#!/bin/bash

# Установка зависимостей
python3 -m pip install --user virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Выполнение скриптов
python3 data_creation.py
python3 model_preprocessing.py
python3 model_preparation.py
python3 model_testing.py > test_results.txt

# Сохранение метрик
echo "Model metrics:" > metrics.txt
echo "MSE: $(grep -oE '[0-9]+\.[0-9]+' test_results.txt | tail -1)" >> metrics.txt
