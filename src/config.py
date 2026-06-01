from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
INBOX_DIR = BASE_DIR / "data" / "inbox"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOGS_DIR = BASE_DIR / "logs"

INBOX_ZIP = RAW_DIR / "inbox.zip"
LOG_FILE = LOGS_DIR / "processing.log"
REPORT_FILE = OUTPUT_DIR / "classification_report.csv"


CATEGORIES = [
    "critical_incident",
    "support_escalation",
    "software_issue",
    "hardware_issue",
    "access_onboarding",
    "finance_billing",
    "document_approval",
    "maintenance_info",
    "spam_phishing",
    "meeting_communication",
    "hr_admin",
    "monitoring_alert",
    "unknown",
    "error",
]
