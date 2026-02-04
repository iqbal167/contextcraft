from contextcraft.service.document_ingest_service import DocumentIngestService

if __name__ == "__main__":
    pdf_path = "/Users/jds/Desktop/contextcraft-workspace/contextcraft/src/contextcraft/tests/fixtures/sample.pdf"

    service = DocumentIngestService()
    document, page_chunks = service.ingest(pdf_path)

    print(f"Document: {document.title}")
    print(f"Pages: {document.page_count}")
    print(f"Size: {document.file_size} bytes")
    print(f"\nPage Chunks: {len(page_chunks)}")

    for chunk in page_chunks:
        print(f"\n--- Page {chunk.page_number} ---")
        print(chunk.text[:200] + "..." if len(chunk.text) > 200 else chunk.text)
