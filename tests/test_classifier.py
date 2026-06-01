import pytest

from src.classifier import EmailClassifier


@pytest.mark.parametrize(
    "email_text, expected_category",
    [
        (
            "У нас критичный инцидент: ошибка 500, работа остановлена",
            "critical_incident",
        ),
        (
            "После обновления браузер Chrome зависает и не открывает файлы",
            "software_issue",
        ),
        (
            "В пятницу плановые технические работы, ряд систем будет недоступен",
            "maintenance_info",
        ),
        (
            "Клиент обращается повторно, заявка висит без ответа уже 3 дня",
            "support_escalation",
        ),
        (
            "Направляем документ на согласование, просим вернуть с правками",
            "document_approval",
        ),
        (
            "Добрый день. Спасибо за информацию.",
            "unknown",
        ),
    ],
)
def test_classifier_categories(email_text, expected_category):
    classifier = EmailClassifier()

    result = classifier.classify(email_text)

    assert result.category == expected_category
    assert result.status == "ok"
