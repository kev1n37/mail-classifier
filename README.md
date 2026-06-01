Наш проект
Проект сортирует входящие письма по категориям.
На входе есть архив data/raw/inbox.zip. Скрипт распаковывает его в data/inbox, программа читает письма, определяет категорию по ключевым словам и копирует файлы в папки внутри data/output.
Структура проектаx:
mail-classifier/
├── data/
│   ├── raw/       исходный архив inbox.zip
│   ├── inbox/     распакованные письма
│   └── output/    результат сортировки
├── logs/          логи обработки
├── src/           основной код
├── tests/         тесты
├── run.sh         запуск проекта
├── requirements.txt
└── README.md

Основные модули:
config.py — хранит пути к папкам и список категорий.
models.py — содержит ClassificationResult, где сохраняются категория, причина и статус обработки.
reader.py — читает письма из .txt файлов. Если файл пустой или формат неподходящий, возникает ошибка.
classifier.py — определяет категорию письма по ключевым словам. Например, ошибка 500 и работа остановлена относятся к critical_incident, а Chrome и браузер — к software_issue.
processor.py — связывает всё вместе: берёт файлы, читает их, классифицирует и копирует в нужные папки.
report.py — создаёт CSV-отчёт classification_report.csv.
main.py — запускает обработку, сохраняет отчёт и выводит статистику.
run.sh — очищает старые данные, распаковывает архив и запускает Python-программу.

Категории:
Мы использовали категории:
critical_incident
support_escalation
software_issue
hardware_issue
access_onboarding
finance_billing
document_approval
maintenance_info
spam_phishing
meeting_communication
hr_admin
monitoring_alert
unknown
error
unknown — если письмо не удалось уверенно классифицировать.
error — если файл невозможно обработать.

Как запустить проект:
1)Установить зависимости: python3 -m pip install -r requirements.txt
2)Запустить проект: bash run.sh
3)После запуска результат будет в папке: data/output/
4)Отчёт будет здесь: data/output/classification_report.csv
5)Лог обработки будет здесь: logs/processing.log
6)Запустить тесты: python3 -m pytest
Тесты проверяют классификацию писем, чтение .txt файлов, пустые файлы и неподдерживаемые форматы.

Кратко про логику:
Программа работает по простому алгоритму:
1. Распаковывает inbox.zip.
2. Читает письма.
3. Ищет ключевые слова.
4. Выбирает категорию.
5. Копирует письмо в нужную папку.
6. Создаёт CSV-отчёт и лог.
