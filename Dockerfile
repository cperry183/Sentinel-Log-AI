# ── Stage 1: dependency builder ───────────────────────────────────────────────
# Use the full image to compile any native wheels (torch, numpy, etc.)
FROM python:3.11-slim AS builder

WORKDIR /build

# System deps needed to compile wheels
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl; \
    rm -rf /var/lib/apt/lists/*

# Copy and install dependencies into an isolated prefix so we can COPY
# only the installed packages into the final stage (no pip cache cruft)
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ── Stage 2: runtime image ────────────────────────────────────────────────────
FROM python:3.11-slim

LABEL org.opencontainers.image.title="Sentinel-Log-AI" \
      org.opencontainers.image.description="BERT-based neural anomaly detection for SRE log monitoring" \
      org.opencontainers.image.source="https://github.com/cperry183/Sentinel-Log-AI" \
      org.opencontainers.image.licenses="GPL-3.0"

# Runtime system deps only (no compilers)
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        libgomp1; \
    rm -rf /var/lib/apt/lists/*

# Pull in the pre-built packages from the builder stage
COPY --from=builder /install /usr/local

# Non-root user — model inference doesn't need elevated privileges
RUN groupadd --gid 1001 sentinel && \
    useradd  --uid 1001 --gid sentinel --shell /bin/bash --create-home sentinel

WORKDIR /app

# Copy source and bundled sample data
COPY src/      ./src/
COPY data/     ./data/

# HuggingFace caches models here by default; keep it inside the container
# home so the non-root user can write to it, and expose it as a volume
# so models survive container restarts without re-downloading.
ENV HF_HOME=/app/.cache/huggingface \
    TRANSFORMERS_CACHE=/app/.cache/huggingface/transformers \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /app/.cache/huggingface && \
    chown -R sentinel:sentinel /app

# Volume for:
#   /app/data    — mount custom log files at runtime
#   /app/.cache  — persist downloaded model weights across runs
VOLUME ["/app/data", "/app/.cache/huggingface"]

USER sentinel

ENTRYPOINT ["python", "src/main.py"]
# Override log file path at runtime:
#   docker run ... sentinel-log-ai --log-file /app/data/my_logs.txt
