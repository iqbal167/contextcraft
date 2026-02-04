from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Note:
    id: str
    document_id: str
    title: str
    content: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
