from pathlib import Path


class EmailReader:
    def read(self, file_path: Path) -> str:
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        if file_path.suffix.lower() != ".txt":
            raise ValueError(f"Неподдерживаемый формат файла: {file_path.suffix}")

        try:
            text = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = file_path.read_text(encoding="cp1251")

        if not text.strip():
            raise ValueError("Письмо пустое")

        return text
