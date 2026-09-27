from datetime import datetime, timezone

# Jinja filters: turn raw database values into text people can read


def duration(minutes):
    """45 -> '45 min', 60 -> '1 h', 390 -> '6 h 30 min'"""
    hours, rest = divmod(int(minutes or 0), 60)
    if not hours:
        return f"{rest} min"
    return f"{hours} h {rest} min" if rest else f"{hours} h"


def iso_duration(minutes):
    """Machine-readable duration for <time datetime="...">: 90 -> 'PT90M'"""
    return f"PT{int(minutes or 0)}M"


def _to_date(timestamp):
    return datetime.fromtimestamp(int(timestamp or 0), tz=timezone.utc)


def date_text(timestamp):
    """1773147767 -> '10 March 2026'"""
    date = _to_date(timestamp)
    return f"{date.day} {date:%B %Y}"


def date_iso(timestamp):
    """1773147767 -> '2026-03-10' for <time datetime="...">"""
    return f"{_to_date(timestamp):%Y-%m-%d}"