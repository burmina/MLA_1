#!/bin/bash
python3 -m data_creation
python3 -m model_preprocessing
python3 -m model_preparation
python3 -m model_testing