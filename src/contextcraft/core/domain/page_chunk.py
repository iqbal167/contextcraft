from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PageChunk:
    document_id: str
    page_number: int
    text: str
    char_count: int
