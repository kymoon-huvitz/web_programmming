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

# 의존성 먼저 복사 후 설치(레이어 캐시 활용)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 비루트 유저 생성(보안)
RUN useradd -m appuser
USER appuser

# Render는 PORT 환경변수 제공. 로컬은 8000 기본값.
EXPOSE 8000

# --- 실행 ---
# run:app -> run.py의 app 객체를 gunicorn이 실행
CMD ["bash", "-lc", "gunicorn -w 3 -k gthread -t 120 -b 0.0.0.0:${PORT:-8000} run:app"]
