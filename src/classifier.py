from src.models import ClassificationResult


class EmailClassifier:
    def __init__(self):
        self.rules = [
            {
                "category": "critical_incident",
                "keywords": [
                    "критичный инцидент",
                    "критический инцидент",
                    "ошибка 500",
                    "работа остановлена",
                    "система недоступна",
                    "сервис недоступен",
                    "упал сервер",
                    "недоступен сервер",
                ],
            },
            {
                "category": "monitoring_alert",
                "keywords": [
                    "alert",
                    "monitoring",
                    "cpu",
                    "memory",
                    "disk",
                    "превышен порог",
                    "алерт",
                    "сработал мониторинг",
                ],
            },
            {
                "category": "spam_phishing",
                "keywords": [
                    "вы выиграли",
                    "казино",
                    "бесплатно",
                    "скидка 90",
                    "перейдите по ссылке",
                    "подтвердите пароль",
                    "введите данные",
                    "срочно подтвердите",
                ],
            },
            {
                "category": "support_escalation",
                "keywords": [
                    "urgent",
                    "повторно",
                    "без ответа",
                    "заявка висит",
                    "срочно разобраться",
                    "второй запрос",
                    "эскалация",
                ],
            },
            {
                "category": "maintenance_info",
                "keywords": [
                    "плановые технические работы",
                    "технические работы",
                    "регламентные работы",
                    "будет недоступен",
                    "будут недоступны",
                    "окно обслуживания",
                ],
            },
            {
                "category": "access_onboarding",
                "keywords": [
                    "доступ",
                    "учетная запись",
                    "учётная запись",
                    "аккаунт",
                    "новый сотрудник",
                    "выдать права",
                    "заблокирован пользователь",
                    "подключить сотрудника",
                    "создать пользователя",
                ],
            },
            {
                "category": "hardware_issue",
                "keywords": [
                    "ноутбук",
                    "монитор",
                    "клавиатура",
                    "мышь",
                    "принтер",
                    "не включается",
                    "сломался",
                    "замена оборудования",
                ],
            },
            {
                "category": "software_issue",
                "keywords": [
                    "chrome",
                    "браузер",
                    "outlook",
                    "excel",
                    "word",
                    "программа",
                    "не открывает",
                    "зависает",
                    "после обновления",
                ],
            },
            {
                "category": "finance_billing",
                "keywords": [
                    "счет",
                    "счёт",
                    "оплата",
                    "invoice",
                    "акт",
                    "закрывающие документы",
                    "возврат",
                    "платеж",
                    "платёж",
                ],
            },
            {
                "category": "document_approval",
                "keywords": [
                    "согласование",
                    "подпись",
                    "договор",
                    "документ",
                    "вернуть с правками",
                    "инструкция на согласование",
                    "проверить условия",
                ],
            },
            {
                "category": "meeting_communication",
                "keywords": [
                    "встреча",
                    "совещание",
                    "созвон",
                    "митинг",
                    "приглашаю",
                    "обсудим",
                    "календарь",
                ],
            },
            {
                "category": "hr_admin",
                "keywords": [
                    "отпуск",
                    "больничный",
                    "кадры",
                    "hr",
                    "командировка",
                    "заявление",
                    "отгул",
                ],
            },
        ]

    def classify(self, text: str) -> ClassificationResult:
        normalized_text = text.lower()

        for rule in self.rules:
            matched_keywords = []

            for keyword in rule["keywords"]:
                if keyword in normalized_text:
                    matched_keywords.append(keyword)

            if matched_keywords:
                return ClassificationResult(
                    category=rule["category"],
                    reason=f"найдены ключевые слова: {', '.join(matched_keywords)}",
                )

        return ClassificationResult(
            category="unknown",
            reason="не найдено подходящих ключевых слов",
        )
