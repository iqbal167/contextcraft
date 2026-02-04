from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Document:
    id: str
    filename: str
    source_path: str
    title: str
    page_count: int
    file_size: int
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
