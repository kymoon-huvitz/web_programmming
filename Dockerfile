# ---- Base ----
FROM python:3.12-slim

# 보안/성능 관련 기본 세팅
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 시스템 패키지(필요 최소)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉터리
WORKDIR /app

# 1) 의존성 먼저 설치 (캐시 최적화)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 2) 비루트 유저 먼저 생성
RUN useradd -m appuser

# 3) 코드 복사할 때부터 소유자를 appuser로 지정  ← 핵심
COPY --chown=appuser:appuser . .

# 4) instance 폴더 보장(있어도 OK) + 소유권 확인  ← 안전장치
RUN mkdir -p /app/instance && chown -R appuser:appuser /app

# 5) 이제부터 비루트로 실행
USER appuser

EXPOSE 8000

CMD ["bash", "-lc", "gunicorn -w 3 -k gthread -t 120 -b 0.0.0.0:${PORT:-8000} run:app"]
