import uuid
from pathlib import Path

from pypdf import PdfReader

from contextcraft.core.domain.document import Document
from contextcraft.core.domain.page_chunk import PageChunk


class DocumentIngestService:
    def ingest(self, file_path: str) -> tuple[Document, list[PageChunk]]:
        path = Path(file_path)
        reader = PdfReader(file_path)

        doc_id = str(uuid.uuid4())
        document = Document(
            id=doc_id,
            filename=path.name,
            source_path=str(path.absolute()),
            title=path.stem,
            page_count=len(reader.pages),
            file_size=path.stat().st_size,
        )

        chunk = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            chunk.append(
                PageChunk(
                    document_id=doc_id,
                    page_number=i + 1,
                    text=text,
                    char_count=len(text),
                )
            )

        return document, chunk
