#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

ZIP_FILE="data/raw/inbox.zip"
INBOX_DIR="data/inbox"
OUTPUT_DIR="data/output"
LOG_DIR="logs"

echo "Запуск проекта mail-classifier"

if [ ! -f "$ZIP_FILE" ]; then
    echo "Ошибка: файл $ZIP_FILE не найден"
    exit 1
fi

echo "Очистка старых данных..."
rm -rf "$INBOX_DIR"
rm -rf "$OUTPUT_DIR"

mkdir -p "$INBOX_DIR"
mkdir -p "$OUTPUT_DIR"
mkdir -p "$LOG_DIR"

echo "Распаковка архива..."
unzip -q "$ZIP_FILE" -d "$INBOX_DIR"

echo "Запуск Python-программы..."
python3 -m src.main

echo "Готово"
echo "Результаты находятся в папке: $OUTPUT_DIR"
echo "Отчёт: $OUTPUT_DIR/classification_report.csv"
echo "Лог: $LOG_DIR/processing.log"
