from pathlib import Path
import logging
import shutil

from src.classifier import EmailClassifier
from src.config import CATEGORIES
from src.reader import EmailReader


class MailProcessor:
    def __init__(self, inbox_dir: Path, output_dir: Path):
        self.inbox_dir = inbox_dir
        self.output_dir = output_dir
        self.reader = EmailReader()
        self.classifier = EmailClassifier()
        self.results = []

    def process_all(self) -> list[dict]:
        self._prepare_output_dirs()

        files = []
        for file_path in self.inbox_dir.rglob("*"):
            if file_path.is_file():
                files.append(file_path)

        logging.info(f"Найдено файлов для обработки: {len(files)}")

        for file_path in files:
            self.process_one(file_path)

        return self.results

    def process_one(self, file_path: Path) -> None:
        try:
            text = self.reader.read(file_path)
            classification = self.classifier.classify(text)

            self._copy_file(file_path, classification.category)

            self.results.append({
                "filename": file_path.name,
                "category": classification.category,
                "status": classification.status,
                "reason": classification.reason,
            })

            message = (
                f"Файл {file_path.name} обработан. "
                f"Категория: {classification.category}. "
                f"Причина: {classification.reason}"
            )
            logging.info(message)

        except Exception as error:
            self._copy_file(file_path, "error")

            self.results.append({
                "filename": file_path.name,
                "category": "error",
                "status": "error",
                "reason": str(error),
            })

            message = f"Файл {file_path.name} не обработан. Ошибка: {error}"
            logging.error(message)

    def _prepare_output_dirs(self) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)

        for category in CATEGORIES:
            category_dir = self.output_dir / category
            category_dir.mkdir(parents=True, exist_ok=True)

    def _copy_file(self, file_path: Path, category: str) -> None:
        target_dir = self.output_dir / category
        target_dir.mkdir(parents=True, exist_ok=True)

        target_path = target_dir / file_path.name
        shutil.copy2(file_path, target_path)
