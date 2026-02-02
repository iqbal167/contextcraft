# ContextCraft

ContextCraft is RAG-powered learning assistant that helps users learn new concepts by providing contextually relevant information from a vast knowledge base.

## Observability

**Structured Logging:**
- Format: `timestamp | level | logger | correlation_id | message`
- Error-aware levels: INFO (2xx/3xx), WARNING (4xx), ERROR (5xx)
- Namespaces: `contextcraft.request`, `contextcraft.error`

**Correlation ID:**
- Tracks requests across RAG pipeline (embedding → search → LLM)
- Client can provide via `X-Correlation-ID` header or auto-generated
- Included in all logs and response headers

## TODO

- Add error logging middleware for unhandled exceptions