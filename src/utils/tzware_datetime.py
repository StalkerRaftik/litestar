from datetime import timezone
import datetime


def tzware_datetime() -> datetime.datetime:
    return datetime.datetime.now(tz=timezone.utc)


__all__ = ["tzware_datetime"]
