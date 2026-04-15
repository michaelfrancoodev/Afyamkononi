from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from core.constants import LANG_SW, CHANNEL_USSD

SESSION_TTL_MINUTES = 10

_store: dict[str, "Session"] = {}


@dataclass
class Session:
    session_id: str
    phone:      str
    channel:    str = CHANNEL_USSD
    lang:       str = LANG_SW
    disease:    str | None = None
    step:       str = "welcome"
    q1:         str | None = None
    q2:         str | None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def touch(self):
        self.updated_at = datetime.now(timezone.utc)

    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) > self.updated_at + timedelta(minutes=SESSION_TTL_MINUTES)


def get(session_id: str) -> Session | None:
    s = _store.get(session_id)
    if s and s.is_expired():
        delete(session_id)
        return None
    return s


def create(session_id: str, phone: str, channel: str = CHANNEL_USSD) -> Session:
    s = Session(session_id=session_id, phone=phone, channel=channel)
    _store[session_id] = s
    return s


def get_or_create(session_id: str, phone: str, channel: str = CHANNEL_USSD) -> Session:
    return get(session_id) or create(session_id, phone, channel)


def update(session: Session):
    session.touch()
    _store[session.session_id] = session


def delete(session_id: str):
    _store.pop(session_id, None)


def purge_expired():
    expired = [sid for sid, s in _store.items() if s.is_expired()]
    for sid in expired:
        del _store[sid]
