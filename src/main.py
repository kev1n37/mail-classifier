import logging
from src.config import INBOX_DIR, OUTPUT_DIR, LOGS_DIR, LOG_FILE, REPORT_FILE
from src.processor import MailProcessor
from src.report import save_report

def setup_logging():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="{asctime} - {levelname} - {message}",
        style="{",
        encoding="utf-8",
    )

def print_statistics(results: list[dict]):
    stats = {}
    for item in results:
        category = item["category"]
        stats[category] = stats.get(category, 0) + 1
    print("\nОбработка завершена")
    print("Статистика:")
    for category, count in sorted(stats.items()):
        print(f"{category}: {count}")

def main():
    setup_logging()
    processor = MailProcessor(inbox_dir=INBOX_DIR, output_dir=OUTPUT_DIR)
    results = processor.process_all()
    save_report(results, REPORT_FILE)
    print_statistics(results)

main()
