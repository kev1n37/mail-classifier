import pytest

from src.reader import EmailReader


def test_read_txt_file(tmp_path):
    file_path = tmp_path / "mail.txt"
    file_path.write_text("Subject: Test email", encoding="utf-8")

    reader = EmailReader()
    text = reader.read(file_path)

    assert text == "Subject: Test email"


def test_empty_file_raises_error(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("", encoding="utf-8")

    reader = EmailReader()

    with pytest.raises(ValueError):
        reader.read(file_path)


def test_non_txt_file_raises_error(tmp_path):
    file_path = tmp_path / "image.jpeg"
    file_path.write_text("not really an image", encoding="utf-8")

    reader = EmailReader()

    with pytest.raises(ValueError):
        reader.read(file_path)
