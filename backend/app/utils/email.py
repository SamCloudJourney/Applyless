from app.core.config import settings


def build_notification_email(subject: str, body: str) -> dict[str, str]:
    return {
        "from": settings.EMAIL_SENDER,
        "subject": subject,
        "body": body,
    }
