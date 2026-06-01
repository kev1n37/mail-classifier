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

        files = sorted(self.inbox_dir.iterdir())

        for file_path in files:
            if file_path.is_file():
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

            logging.info(
                "%s -> %s | %s",
                file_path.name,
                classification.category,
                classification.reason,
            )

        except Exception as error:
            self._copy_file(file_path, "error")

            self.results.append({
                "filename": file_path.name,
                "category": "error",
                "status": "error",
                "reason": str(error),
            })

            logging.error("%s -> error | %s", file_path.name, error)

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
